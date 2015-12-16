# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Show.slug'
        db.add_column(u'tickets_show', 'slug',
                      self.gf('django.db.models.fields.SlugField')(default='FAIL', max_length=50),
                      keep_default=False)


        # Changing field 'Show.end_date'
        db.alter_column(u'tickets_show', 'end_date', self.gf('django.db.models.fields.DateField')(default=datetime.datetime(1, 1, 1, 0, 0)))

        # Changing field 'Show.start_date'
        db.alter_column(u'tickets_show', 'start_date', self.gf('django.db.models.fields.DateField')(default=datetime.datetime(1, 1, 1, 0, 0)))

    def backwards(self, orm):
        # Deleting field 'Show.slug'
        db.delete_column(u'tickets_show', 'slug')


        # Changing field 'Show.end_date'
        db.alter_column(u'tickets_show', 'end_date', self.gf('django.db.models.fields.DateField')(null=True))

        # Changing field 'Show.start_date'
        db.alter_column(u'tickets_show', 'start_date', self.gf('django.db.models.fields.DateField')(null=True))

    models = {
        u'tickets.category': {
            'Meta': {'object_name': 'Category'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50'}),
            'sort': ('django.db.models.fields.IntegerField', [], {})
        },
        u'tickets.occurrence': {
            'Meta': {'object_name': 'Occurrence'},
            'date': ('django.db.models.fields.DateField', [], {}),
            'hours_til_close': ('django.db.models.fields.IntegerField', [], {'default': '2'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'maximum_sell': ('django.db.models.fields.PositiveIntegerField', [], {'default': '80'}),
            'show': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['tickets.Show']"}),
            'time': ('django.db.models.fields.TimeField', [], {'default': 'datetime.time(19, 0)'})
        },
        u'tickets.show': {
            'Meta': {'object_name': 'Show'},
            'category': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['tickets.Category']"}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'end_date': ('django.db.models.fields.DateField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'location': ('django.db.models.fields.CharField', [], {'default': "'New Theatre'", 'max_length': '30'}),
            'long_description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'poster': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'poster_page': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'poster_tiny': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'poster_wall': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50'}),
            'start_date': ('django.db.models.fields.DateField', [], {})
        },
        u'tickets.ticket': {
            'Meta': {'object_name': 'Ticket'},
            'cancelled': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'email_address': ('django.db.models.fields.EmailField', [], {'max_length': '80'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'occurrence': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['tickets.Occurrence']"}),
            'person_name': ('django.db.models.fields.CharField', [], {'max_length': '80'}),
            'quantity': ('django.db.models.fields.IntegerField', [], {'default': '1'}),
            'stamp': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'unique_code': ('django.db.models.fields.CharField', [], {'max_length': '16'})
        }
    }

    complete_apps = ['tickets']