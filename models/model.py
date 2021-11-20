# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Anggota(models.Model):
    _name = 'anggota.anggota' # membuat tabel anggota_anggota pada postgres 
    _description = 'Data Anggota' # deskripsi tabel

    id = fields.Integer(string="ID", required=True)
    name = fields.Char(string="Nama", required=True)
    department = fields.Selection(selection=[
        ('0', 'Ketua (G1)'), 
        ('1', 'Koordinator Akhwat (A1)'), 
        ('2', 'Kesekjenan'), 
        ('3', 'Kewilayahan'), 
        ('4', 'PSDM'), 
        ('5', 'SPDK'), 
        ('6', 'Eksternal'), 
        ('7', 'Annissa'), 
    ], string="Departemen", required=True)

class Riwayat(models.Model):
    _name = 'riwayat.riwayat' # membuat tabel riwayat pada postgres 
    _description = 'Data riwayat' # deskripsi tabel