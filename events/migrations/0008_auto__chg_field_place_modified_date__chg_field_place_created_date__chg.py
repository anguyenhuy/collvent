# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Place.modified_date'
        db.alter_column(u'events_place', 'modified_date', self.gf('django.db.models.fields.DateTimeField')())

        # Changing field 'Place.created_date'
        db.alter_column(u'events_place', 'created_date', self.gf('django.db.models.fields.DateTimeField')())

        # Changing field 'Place.deleted_date'
        db.alter_column(u'events_place', 'deleted_date', self.gf('django.db.models.fields.DateTimeField')(null=True))

        # Changing field 'Event.modified_date'
        db.alter_column(u'events_event', 'modified_date', self.gf('django.db.models.fields.DateTimeField')())

        # Changing field 'Event.created_date'
        db.alter_column(u'events_event', 'created_date', self.gf('django.db.models.fields.DateTimeField')())

        # Changing field 'Event.deleted_date'
        db.alter_column(u'events_event', 'deleted_date', self.gf('django.db.models.fields.DateTimeField')(null=True))

        # Changing field 'Invitation.modified_date'
        db.alter_column(u'events_invitation', 'modified_date', self.gf('django.db.models.fields.DateTimeField')())

        # Changing field 'Invitation.created_date'
        db.alter_column(u'events_invitation', 'created_date', self.gf('django.db.models.fields.DateTimeField')())

        # Changing field 'Invitation.deleted_date'
        db.alter_column(u'events_invitation', 'deleted_date', self.gf('django.db.models.fields.DateTimeField')(null=True))

    def backwards(self, orm):

        # Changing field 'Place.modified_date'
        db.alter_column(u'events_place', 'modified_date', self.gf('django.db.models.fields.DateField')())

        # Changing field 'Place.created_date'
        db.alter_column(u'events_place', 'created_date', self.gf('django.db.models.fields.DateField')())

        # Changing field 'Place.deleted_date'
        db.alter_column(u'events_place', 'deleted_date', self.gf('django.db.models.fields.DateField')(null=True))

        # Changing field 'Event.modified_date'
        db.alter_column(u'events_event', 'modified_date', self.gf('django.db.models.fields.DateField')())

        # Changing field 'Event.created_date'
        db.alter_column(u'events_event', 'created_date', self.gf('django.db.models.fields.DateField')())

        # Changing field 'Event.deleted_date'
        db.alter_column(u'events_event', 'deleted_date', self.gf('django.db.models.fields.DateField')(null=True))

        # Changing field 'Invitation.modified_date'
        db.alter_column(u'events_invitation', 'modified_date', self.gf('django.db.models.fields.DateField')())

        # Changing field 'Invitation.created_date'
        db.alter_column(u'events_invitation', 'created_date', self.gf('django.db.models.fields.DateField')())

        # Changing field 'Invitation.deleted_date'
        db.alter_column(u'events_invitation', 'deleted_date', self.gf('django.db.models.fields.DateField')(null=True))

    models = {
        u'accounts.user': {
            'Meta': {'object_name': 'User'},
            'avatar': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'email': ('django.db.models.fields.EmailField', [], {'db_index': 'True', 'max_length': '255', 'unique': 'True', 'null': 'True', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '31'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_admin': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '31'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'phone': ('django.db.models.fields.CharField', [], {'db_index': 'True', 'max_length': '31', 'unique': 'True', 'null': 'True', 'blank': 'True'}),
            'uuid': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255', 'db_index': 'True'})
        },
        u'events.event': {
            'Meta': {'object_name': 'Event'},
            'created_by': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'created_date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'deleted_by': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'deleted_date': ('django.db.models.fields.DateTimeField', [], {'default': 'None', 'null': 'True', 'db_index': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'max_length': '512'}),
            'end_date': ('django.db.models.fields.DateTimeField', [], {'null': 'True'}),
            'host': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['accounts.User']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'location': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['events.Place']"}),
            'modified_by': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'modified_date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'start_date': ('django.db.models.fields.DateTimeField', [], {'null': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'uuid': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'events.invitation': {
            'Meta': {'object_name': 'Invitation'},
            'created_by': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'created_date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'deleted_by': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'deleted_date': ('django.db.models.fields.DateTimeField', [], {'default': 'None', 'null': 'True', 'db_index': 'True'}),
            'event': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['events.Event']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified_by': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'modified_date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['accounts.User']"})
        },
        u'events.place': {
            'Meta': {'object_name': 'Place'},
            'city': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'created_by': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'created_date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'deleted_by': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'deleted_date': ('django.db.models.fields.DateTimeField', [], {'default': 'None', 'null': 'True', 'db_index': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'latitude': ('django.db.models.fields.CharField', [], {'max_length': '31', 'null': 'True'}),
            'longitude': ('django.db.models.fields.CharField', [], {'max_length': '31', 'null': 'True'}),
            'modified_by': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'modified_date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'state': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'street_addr': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'zip_code': ('django.db.models.fields.IntegerField', [], {'null': 'True'})
        }
    }

    complete_apps = ['events']