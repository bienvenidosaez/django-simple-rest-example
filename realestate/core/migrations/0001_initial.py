# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Adv'
        db.create_table(u'core_adv', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('date', self.gf('django.db.models.fields.DateField')()),
            ('type', self.gf('django.db.models.fields.IntegerField')()),
            ('price', self.gf('django.db.models.fields.IntegerField')()),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['core.User'])),
        ))
        db.send_create_signal(u'core', ['Adv'])

        # Adding M2M table for field obj on 'Adv'
        db.create_table(u'core_adv_obj', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('adv', models.ForeignKey(orm[u'core.adv'], null=False)),
            ('object', models.ForeignKey(orm[u'core.object'], null=False))
        ))
        db.create_unique(u'core_adv_obj', ['adv_id', 'object_id'])

        # Adding model 'Object'
        db.create_table(u'core_object', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('key_feature', self.gf('django.db.models.fields.CharField')(max_length=20L)),
            ('value_feature', self.gf('django.db.models.fields.CharField')(max_length=20L)),
        ))
        db.send_create_signal(u'core', ['Object'])

        # Adding model 'VCard'
        db.create_table(u'core_vcard', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('vcard_name', self.gf('django.db.models.fields.CharField')(max_length=20L)),
            ('date', self.gf('django.db.models.fields.DateField')()),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['core.User'])),
        ))
        db.send_create_signal(u'core', ['VCard'])

        # Adding M2M table for field requirements on 'VCard'
        db.create_table(u'core_vcard_requirements', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('vcard', models.ForeignKey(orm[u'core.vcard'], null=False)),
            ('vcardrequirement', models.ForeignKey(orm[u'core.vcardrequirement'], null=False))
        ))
        db.create_unique(u'core_vcard_requirements', ['vcard_id', 'vcardrequirement_id'])

        # Adding model 'VCardRequirement'
        db.create_table(u'core_vcardrequirement', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('key_feature', self.gf('django.db.models.fields.CharField')(max_length=20L)),
            ('value_feature', self.gf('django.db.models.fields.CharField')(max_length=20L)),
        ))
        db.send_create_signal(u'core', ['VCardRequirement'])

        # Adding model 'Message'
        db.create_table(u'core_message', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('adv', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['core.Adv'])),
            ('user_ins', self.gf('django.db.models.fields.related.ForeignKey')(related_name='recipient', to=orm['core.User'])),
            ('user_read', self.gf('django.db.models.fields.related.ForeignKey')(related_name='sender', to=orm['core.User'])),
            ('date', self.gf('django.db.models.fields.DateField')()),
            ('message', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal(u'core', ['Message'])

        # Adding model 'FriendList'
        db.create_table(u'core_friendlist', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('id_friend', self.gf('django.db.models.fields.IntegerField')()),
            ('id_user', self.gf('django.db.models.fields.IntegerField')()),
            ('key_feature', self.gf('django.db.models.fields.CharField')(max_length=20L)),
            ('value_feature', self.gf('django.db.models.fields.CharField')(max_length=20L)),
            ('social', self.gf('django.db.models.fields.CharField')(max_length=15L)),
        ))
        db.send_create_signal(u'core', ['FriendList'])

        # Adding unique constraint on 'FriendList', fields ['id_friend', 'social']
        db.create_unique(u'core_friendlist', ['id_friend', 'social'])

        # Adding model 'User'
        db.create_table(u'core_user', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('password', self.gf('django.db.models.fields.CharField')(max_length=128)),
            ('last_login', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now)),
            ('username', self.gf('django.db.models.fields.CharField')(unique=True, max_length=20L)),
            ('email', self.gf('django.db.models.fields.CharField')(max_length=40L)),
            ('first_name', self.gf('django.db.models.fields.CharField')(max_length=20L)),
            ('last_name', self.gf('django.db.models.fields.CharField')(max_length=20L)),
            ('photo', self.gf('django.db.models.fields.CharField')(max_length=50L)),
            ('city', self.gf('django.db.models.fields.CharField')(max_length=20L)),
            ('phone', self.gf('django.db.models.fields.CharField')(max_length=15L)),
            ('registration_date', self.gf('django.db.models.fields.DateTimeField')()),
        ))
        db.send_create_signal(u'core', ['User'])


    def backwards(self, orm):
        # Removing unique constraint on 'FriendList', fields ['id_friend', 'social']
        db.delete_unique(u'core_friendlist', ['id_friend', 'social'])

        # Deleting model 'Adv'
        db.delete_table(u'core_adv')

        # Removing M2M table for field obj on 'Adv'
        db.delete_table('core_adv_obj')

        # Deleting model 'Object'
        db.delete_table(u'core_object')

        # Deleting model 'VCard'
        db.delete_table(u'core_vcard')

        # Removing M2M table for field requirements on 'VCard'
        db.delete_table('core_vcard_requirements')

        # Deleting model 'VCardRequirement'
        db.delete_table(u'core_vcardrequirement')

        # Deleting model 'Message'
        db.delete_table(u'core_message')

        # Deleting model 'FriendList'
        db.delete_table(u'core_friendlist')

        # Deleting model 'User'
        db.delete_table(u'core_user')


    models = {
        u'core.adv': {
            'Meta': {'object_name': 'Adv'},
            'date': ('django.db.models.fields.DateField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'obj': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['core.Object']", 'symmetrical': 'False'}),
            'price': ('django.db.models.fields.IntegerField', [], {}),
            'type': ('django.db.models.fields.IntegerField', [], {}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['core.User']"})
        },
        u'core.friendlist': {
            'Meta': {'unique_together': "(('id_friend', 'social'),)", 'object_name': 'FriendList'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'id_friend': ('django.db.models.fields.IntegerField', [], {}),
            'id_user': ('django.db.models.fields.IntegerField', [], {}),
            'key_feature': ('django.db.models.fields.CharField', [], {'max_length': '20L'}),
            'social': ('django.db.models.fields.CharField', [], {'max_length': '15L'}),
            'value_feature': ('django.db.models.fields.CharField', [], {'max_length': '20L'})
        },
        u'core.message': {
            'Meta': {'object_name': 'Message'},
            'adv': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['core.Adv']"}),
            'date': ('django.db.models.fields.DateField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'message': ('django.db.models.fields.TextField', [], {}),
            'user_ins': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'recipient'", 'to': u"orm['core.User']"}),
            'user_read': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'sender'", 'to': u"orm['core.User']"})
        },
        u'core.object': {
            'Meta': {'object_name': 'Object'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'key_feature': ('django.db.models.fields.CharField', [], {'max_length': '20L'}),
            'value_feature': ('django.db.models.fields.CharField', [], {'max_length': '20L'})
        },
        u'core.user': {
            'Meta': {'object_name': 'User'},
            'city': ('django.db.models.fields.CharField', [], {'max_length': '20L'}),
            'email': ('django.db.models.fields.CharField', [], {'max_length': '40L'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '20L'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '20L'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '15L'}),
            'photo': ('django.db.models.fields.CharField', [], {'max_length': '50L'}),
            'registration_date': ('django.db.models.fields.DateTimeField', [], {}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '20L'})
        },
        u'core.vcard': {
            'Meta': {'object_name': 'VCard'},
            'date': ('django.db.models.fields.DateField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'requirements': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['core.VCardRequirement']", 'symmetrical': 'False'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['core.User']"}),
            'vcard_name': ('django.db.models.fields.CharField', [], {'max_length': '20L'})
        },
        u'core.vcardrequirement': {
            'Meta': {'object_name': 'VCardRequirement'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'key_feature': ('django.db.models.fields.CharField', [], {'max_length': '20L'}),
            'value_feature': ('django.db.models.fields.CharField', [], {'max_length': '20L'})
        }
    }

    complete_apps = ['core']