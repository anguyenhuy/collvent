from django.http import HttpResponse, HttpResponseBadRequest
from django.core.validators import validate_email
from django.core.exceptions import ValidationError

import base.api.base as base
import accounts.models as accounts_models
import accounts.lib.user as user_lib

class UserCreateApi(base.RestView):

    model = accounts_models.User

    def POST(self, request, *args, **kwargs):
        if 'first_name' not in request.POST or not request.POST['first_name']:
            return HttpResponseBadRequest('Please provide your first name.')
        if 'last_name' not in request.POST or not request.POST['last_name']:
            return HttpResponseBadRequest('Please provide your last name.')
        if ('email' not in request.POST or not request.POST['email']) and \
           ('phone' not in request.POST or not request.POST['phone']):
            return HttpResponseBadRequest('Please submit either an email or a phone number.')
        if 'password' not in request.POST or not request.POST['password']:
            return HttpResponseBadRequest('A password is required.')
        email = request.POST['email']
        phone = request.POST['phone']
        password = request.POST['password']
        try:
            user_lib.validate_password(password)
        except ValidationError:
            return HttpResponseBadRequest('Your password must be at least 6 characters.')
        try:
            if email: validate_email(email)
            if phone: phone = user_lib.clean_us_phone_number(phone)
            user = accounts_models.User.objects.get(email=email)
        except ValidationError:
            return HttpResponseBadRequest('The email or phone number you have submitted is not valid.')
        except accounts_models.User.DoesNotExist:
            try:
                user = accounts_models.User.objects.get(phone=phone)
            except accounts_models.User.DoesNotExist:
                new_user = accounts_models.User.objects.create_user(
                    email=email,
                    phone=phone,
                    password=password,
                    first_name=request.POST['first_name'].lower(),
                    last_name=request.POST['last_name'].lower()
                )
                return HttpResponse()
        if not user.password_set:
            user_lib.update_user(user, email, phone, password)
            return HttpResponse()
        else: return HttpResponseBadRequest('User account already exists.')

class UserApi(base.RestView):
    def PUT(self, request, user_uuid, *args, **kwargs):
        try:
            user = accounts_models.User.objects.get(uuid=user_uuid)
        except accounts_models.User.DoesNotExist:
            return HttpResponseBadRequest('User could not be found.')
        if 'password' in request.POST and request.POST['password']:
            password = request.POST['password']
            try:
                user_lib.validate_password(password)
            except ValidationError:
                return HttpResponseBadRequest('Your password must be at least 6 characters.')
            user.set_password(password)
        user.save()
        return HttpResponse()
