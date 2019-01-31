# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-11-28 15:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feedback', '0002_auto_20170323_1337'),
    ]

    operations = [
        migrations.AlterField(
            model_name='missingsignfeedback',
            name='althandshape',
            field=models.IntegerField(blank=True, choices=[('0', '-'), ('1', 'N/A'), ('15', '1'), ('21', '1_curved'), ('37', '3'), ('191', '3 > O'), ('200', '3_curved'), ('35', '4'), ('201', '4 > 5'), ('192', '4 > O'), ('3', '5'), ('205', '5_claw'), ('203', '5_lax'), ('207', '5i'), ('30', '5m'), ('43', '5m_closed'), ('2', '5m_open'), ('19', '5r'), ('49', '5r_closed'), ('48', '9'), ('24', 'A'), ('153', 'A > 5'), ('195', 'A > O'), ('2', 'A > T'), ('6', 'B'), ('173', 'B > A'), ('174', 'B > L'), ('175', 'B > S'), ('176', 'B > middlefinger'), ('138', 'B+1'), ('26', 'B_bent'), ('170', 'B_bent > B'), ('13', 'B_curved'), ('62', 'Baby_C'), ('206', 'Baby_C_extended'), ('38', 'Baby_O'), ('29', 'Baby_beak'), ('155', 'Baby_beak > A'), ('83', 'Baby_beak_open'), ('22', 'Beak'), ('17', 'Beak2'), ('85', 'Beak2_open'), ('152', 'Beak2_open_spread'), ('84', 'Beak_open'), ('87', 'Beak_open_spread'), ('86', 'Beak_spread'), ('27', 'C'), ('145', 'C > I'), ('136', 'C2_closed'), ('75', 'C2_spread'), ('12', 'C_spread'), ('34', 'D'), ('172', 'E'), ('39', 'F'), ('177', 'F > L'), ('197', 'Flower'), ('199', 'Flower > Beak_open_spread'), ('178', 'G'), ('59', 'Horns'), ('25', 'I'), ('181', 'I > L'), ('196', 'I > N'), ('182', 'I > W'), ('198', 'ILY'), ('179', 'K'), ('9', 'L'), ('193', 'L > O'), ('52', 'L2'), ('40', 'M'), ('183', 'M > V'), ('202', 'MRP'), ('80', 'Middle finger'), ('209', 'Middle finger > I'), ('4', 'Money'), ('14', 'N'), ('142', 'N > B'), ('184', 'N > E'), ('32', 'O'), ('139', 'O > 5m'), ('185', 'O > K'), ('135', 'Other'), ('180', 'P'), ('18', 'Q'), ('47', 'R'), ('8', 'S'), ('186', 'S > I'), ('204', 'S > L'), ('208', 'S > V'), ('28', 'T'), ('187', 'T > L'), ('188', 'T > V'), ('154', 'T_open'), ('5', 'V'), ('20', 'V_curved'), ('190', 'Variable'), ('16', 'W'), ('194', 'W > Beak2'), ('7', 'Y'), ('189', 'Y > R')], default=0),
        ),
        migrations.AlterField(
            model_name='missingsignfeedback',
            name='direction',
            field=models.IntegerField(blank=True, choices=[('0', '-'), ('1', 'N/A'), ('5', 'Backwards'), ('103', 'Backwards + contralateral'), ('87', 'Backwards + downwards'), ('93', 'Backwards + ipsilateral'), ('72', 'Backwards + upwards'), ('6', 'Backwards > downwards'), ('2', 'Backwards > forwards'), ('15', 'Backwards/forwards'), ('50', 'Contralateral'), ('53', 'Contralateral + downwards'), ('54', 'Contralateral + forwards'), ('52', 'Contralateral + upwards'), ('3', 'Contralateral > forwards'), ('102', 'Contralateral > ipsilateral'), ('98', 'Distal'), ('8', 'Downwards'), ('105', 'Downwards + contralateral/ipsilateral'), ('56', 'Downwards + forwards'), ('57', 'Downwards + ipsilateral'), ('58', 'Downwards + ipsilateral > downwards'), ('94', 'Downwards + towards'), ('59', 'Downwards > contralateral'), ('4', 'Downwards > forwards'), ('55', 'Downwards > ipsilateral'), ('104', 'Downwards > upwards'), ('69', 'Downwards/upwards'), ('90', 'Downwards/upwards + ipsilateral'), ('16', 'Forwards'), ('60', 'Forwards + ipsilateral'), ('61', 'Forwards + upwards'), ('63', 'Forwards > contralateral'), ('17', 'Forwards > downwards'), ('62', 'Forwards > ipsilateral'), ('64', 'Forwards > ipsilateral > forwards'), ('92', 'Forwards > upwards'), ('100', 'From location'), ('51', 'Ipsilateral'), ('91', 'Ipsilateral + up and down'), ('65', 'Ipsilateral + upwards'), ('71', 'Ipsilateral > contralateral'), ('68', 'Ipsilateral > downwards'), ('66', 'Ipsilateral > downwards > contralateral'), ('67', 'Ipsilateral > upwards'), ('89', 'Ipsilateral and contralateral'), ('88', 'Ipsilateral/contralateral'), ('99', 'Lateral'), ('95', 'Proximal'), ('46', 'To and fro'), ('96', 'Towards location'), ('70', 'Up and down'), ('32', 'Upwards'), ('33', 'Upwards > downwards'), ('73', 'Upwards > forwards > downwards'), ('49', 'Variable')], default=0),
        ),
        migrations.AlterField(
            model_name='missingsignfeedback',
            name='handbodycontact',
            field=models.IntegerField(blank=True, choices=[('0', '-'), ('1', 'N/A'), ('2', 'Brush'), ('6', 'Continuous'), ('15', 'Continuous > continuous'), ('8', 'Continuous > final'), ('13', 'Continuous > none'), ('12', 'Double'), ('4', 'Final'), ('14', 'Final > continuous'), ('16', 'Final > none'), ('5', 'Initial'), ('11', 'None > final'), ('9', 'None > initial')], default=0),
        ),
        migrations.AlterField(
            model_name='missingsignfeedback',
            name='handform',
            field=models.IntegerField(blank=True, choices=[('0', '-'), ('1', 'N/A'), ('2', '1'), ('4', '2a'), ('7', '2n'), ('5', '2s'), ('6', 'X')], default=0),
        ),
        migrations.AlterField(
            model_name='missingsignfeedback',
            name='handinteraction',
            field=models.IntegerField(blank=True, choices=[('0', '-'), ('1', 'N/A'), ('45', 'Above'), ('47', 'Above/below'), ('50', 'Around'), ('43', 'Back'), ('46', 'Below'), ('41', 'Cross'), ('42', 'Front'), ('44', 'Front/back'), ('48', 'Inside'), ('27', 'Interlocked'), ('40', 'Interwoven'), ('49', 'Next-to')], default=0),
        ),
        migrations.AlterField(
            model_name='missingsignfeedback',
            name='handshape',
            field=models.IntegerField(blank=True, choices=[('0', '-'), ('1', 'N/A'), ('15', '1'), ('21', '1_curved'), ('37', '3'), ('191', '3 > O'), ('200', '3_curved'), ('35', '4'), ('201', '4 > 5'), ('192', '4 > O'), ('3', '5'), ('205', '5_claw'), ('203', '5_lax'), ('207', '5i'), ('30', '5m'), ('43', '5m_closed'), ('2', '5m_open'), ('19', '5r'), ('49', '5r_closed'), ('48', '9'), ('24', 'A'), ('153', 'A > 5'), ('195', 'A > O'), ('2', 'A > T'), ('6', 'B'), ('173', 'B > A'), ('174', 'B > L'), ('175', 'B > S'), ('176', 'B > middlefinger'), ('138', 'B+1'), ('26', 'B_bent'), ('170', 'B_bent > B'), ('13', 'B_curved'), ('62', 'Baby_C'), ('206', 'Baby_C_extended'), ('38', 'Baby_O'), ('29', 'Baby_beak'), ('155', 'Baby_beak > A'), ('83', 'Baby_beak_open'), ('22', 'Beak'), ('17', 'Beak2'), ('85', 'Beak2_open'), ('152', 'Beak2_open_spread'), ('84', 'Beak_open'), ('87', 'Beak_open_spread'), ('86', 'Beak_spread'), ('27', 'C'), ('145', 'C > I'), ('136', 'C2_closed'), ('75', 'C2_spread'), ('12', 'C_spread'), ('34', 'D'), ('172', 'E'), ('39', 'F'), ('177', 'F > L'), ('197', 'Flower'), ('199', 'Flower > Beak_open_spread'), ('178', 'G'), ('59', 'Horns'), ('25', 'I'), ('181', 'I > L'), ('196', 'I > N'), ('182', 'I > W'), ('198', 'ILY'), ('179', 'K'), ('9', 'L'), ('193', 'L > O'), ('52', 'L2'), ('40', 'M'), ('183', 'M > V'), ('202', 'MRP'), ('80', 'Middle finger'), ('209', 'Middle finger > I'), ('4', 'Money'), ('14', 'N'), ('142', 'N > B'), ('184', 'N > E'), ('32', 'O'), ('139', 'O > 5m'), ('185', 'O > K'), ('135', 'Other'), ('180', 'P'), ('18', 'Q'), ('47', 'R'), ('8', 'S'), ('186', 'S > I'), ('204', 'S > L'), ('208', 'S > V'), ('28', 'T'), ('187', 'T > L'), ('188', 'T > V'), ('154', 'T_open'), ('5', 'V'), ('20', 'V_curved'), ('190', 'Variable'), ('16', 'W'), ('194', 'W > Beak2'), ('7', 'Y'), ('189', 'Y > R')], default=0),
        ),
        migrations.AlterField(
            model_name='missingsignfeedback',
            name='location',
            field=models.IntegerField(blank=True, choices=[('0', '-'), ('1', 'N/A'), ('21', 'Arm'), ('128', 'Armpit'), ('83', 'Back'), ('37', 'Back of head'), ('26', 'Belly'), ('14', 'Belly + forehead'), ('132', 'Belly > chest'), ('147', 'Between collarbones'), ('148', 'Between fingers'), ('143', 'Between legs'), ('2', 'Bottom'), ('149', 'Bottom/crotch'), ('135', 'Breasts'), ('136', 'Breasts_ipsi'), ('130', 'Bridge of the nose'), ('23', 'Cheek'), ('138', 'Cheek > cheek'), ('108', 'Cheek > chin'), ('72', 'Cheek contra'), ('16', 'Cheekbone'), ('8', 'Chest'), ('35', 'Chest > trunk'), ('74', 'Chest contra'), ('12', 'Chin'), ('70', 'Chin > chest'), ('28', 'Chin > neutral space'), ('102', 'Chin > weak hand: index finger'), ('33', 'Chin > weak hand: palm'), ('117', 'Chin > weak hand: thumb side'), ('133', 'Chin contra'), ('144', 'Crotch'), ('18', 'Ear'), ('84', 'Ear > cheek'), ('124', 'Ear > chest'), ('140', 'Earlobe'), ('142', 'East'), ('77', 'Elbow'), ('15', 'Eye'), ('120', 'Eye > neutral space'), ('129', 'Eyebrow'), ('17', 'Face'), ('110', 'Face > head'), ('93', 'Flank'), ('145', 'Flank/head'), ('7', 'Forehead'), ('34', 'Forehead > chest'), ('31', 'Forehead > chin'), ('106', 'Forehead > neutral space'), ('134', 'Forehead > shoulder'), ('104', 'Forehead > weak hand: palm'), ('64', 'Forehead contra'), ('10', 'Head'), ('119', 'Head + neutral space'), ('113', 'Head > chest'), ('127', 'Head > chest > shoulder'), ('69', 'Head > neutral space'), ('32', 'Head > shoulder'), ('107', 'Head > weak hand: palm'), ('150', 'Head contra'), ('30', 'Head ipsi'), ('94', 'Hip'), ('92', 'Horizontal plane'), ('85', 'Knee'), ('45', 'Leg'), ('151', 'Leg > waist'), ('95', 'Lower arm'), ('19', 'Mouth'), ('114', 'Mouth > cheek'), ('48', 'Mouth > chest'), ('13', 'Mouth > chin'), ('58', 'Mouth > weak hand'), ('112', 'Mouth > weak hand: palm'), ('152', 'Mouth contra'), ('137', 'Mouth ipsi'), ('9', 'Neck'), ('52', 'Neck > chest'), ('75', 'Neck contra'), ('3', 'Neutral space'), ('2', 'Neutral space > head'), ('121', 'Neutral space > nose'), ('29', 'Neutral space/weak hand: front'), ('22', 'Nose'), ('103', 'Nose > chin'), ('122', 'Nose > neutral space'), ('116', 'Parallel plane'), ('125', 'R-loc'), ('126', 'R-loc > R-loc'), ('4', 'Shoulder'), ('153', 'Shoulder > chest'), ('115', 'Shoulder > shoulder'), ('123', 'Shoulder > weak hand: palm'), ('55', 'Shoulder contra'), ('131', 'Teeth'), ('146', 'Teeth'), ('43', 'Temple'), ('78', 'Temple > chest'), ('79', 'Thumb'), ('27', 'Tongue'), ('97', 'Trunk'), ('54', 'Upper arm'), ('63', 'Upper lip'), ('118', 'Variable'), ('91', 'Virtual object'), ('5', 'Weak hand'), ('6', 'Weak hand > arm'), ('11', 'Weak hand: back'), ('109', 'Weak hand: base'), ('66', 'Weak hand: finger tips'), ('210', 'Weak hand: fingers'), ('90', 'Weak hand: front'), ('96', 'Weak hand: index finger'), ('98', 'Weak hand: middle finger'), ('36', 'Weak hand: palm'), ('88', 'Weak hand: pinkie'), ('101', 'Weak hand: pinkie side'), ('99', 'Weak hand: ring finger'), ('139', 'Weak hand: thenar'), ('59', 'Weak hand: thumb'), ('100', 'Weak hand: thumb side'), ('111', 'Weak hand: thumb side > arm'), ('89', 'Weak hand: web space'), ('141', 'West'), ('50', 'Wrist')], default=0),
        ),
        migrations.AlterField(
            model_name='missingsignfeedback',
            name='movementtype',
            field=models.IntegerField(blank=True, choices=[('0', '-'), ('1', 'N/A'), ('4', 'Arc'), ('37', 'Circle'), ('46', 'Cross'), ('44', 'Motivated shape'), ('45', 'Spiral'), ('6', 'Straight'), ('12', 'Zigzag')], default=0),
        ),
        migrations.AlterField(
            model_name='missingsignfeedback',
            name='relativelocation',
            field=models.IntegerField(blank=True, choices=[('0', '-'), ('1', 'N/A'), ('21', 'Arm'), ('128', 'Armpit'), ('83', 'Back'), ('37', 'Back of head'), ('26', 'Belly'), ('14', 'Belly + forehead'), ('132', 'Belly > chest'), ('147', 'Between collarbones'), ('148', 'Between fingers'), ('143', 'Between legs'), ('2', 'Bottom'), ('149', 'Bottom/crotch'), ('135', 'Breasts'), ('136', 'Breasts_ipsi'), ('130', 'Bridge of the nose'), ('23', 'Cheek'), ('138', 'Cheek > cheek'), ('108', 'Cheek > chin'), ('72', 'Cheek contra'), ('16', 'Cheekbone'), ('8', 'Chest'), ('35', 'Chest > trunk'), ('74', 'Chest contra'), ('12', 'Chin'), ('70', 'Chin > chest'), ('28', 'Chin > neutral space'), ('102', 'Chin > weak hand: index finger'), ('33', 'Chin > weak hand: palm'), ('117', 'Chin > weak hand: thumb side'), ('133', 'Chin contra'), ('144', 'Crotch'), ('18', 'Ear'), ('84', 'Ear > cheek'), ('124', 'Ear > chest'), ('140', 'Earlobe'), ('142', 'East'), ('77', 'Elbow'), ('15', 'Eye'), ('120', 'Eye > neutral space'), ('129', 'Eyebrow'), ('17', 'Face'), ('110', 'Face > head'), ('93', 'Flank'), ('145', 'Flank/head'), ('7', 'Forehead'), ('34', 'Forehead > chest'), ('31', 'Forehead > chin'), ('106', 'Forehead > neutral space'), ('134', 'Forehead > shoulder'), ('104', 'Forehead > weak hand: palm'), ('64', 'Forehead contra'), ('10', 'Head'), ('119', 'Head + neutral space'), ('113', 'Head > chest'), ('127', 'Head > chest > shoulder'), ('69', 'Head > neutral space'), ('32', 'Head > shoulder'), ('107', 'Head > weak hand: palm'), ('150', 'Head contra'), ('30', 'Head ipsi'), ('94', 'Hip'), ('92', 'Horizontal plane'), ('85', 'Knee'), ('45', 'Leg'), ('151', 'Leg > waist'), ('95', 'Lower arm'), ('19', 'Mouth'), ('114', 'Mouth > cheek'), ('48', 'Mouth > chest'), ('13', 'Mouth > chin'), ('58', 'Mouth > weak hand'), ('112', 'Mouth > weak hand: palm'), ('152', 'Mouth contra'), ('137', 'Mouth ipsi'), ('9', 'Neck'), ('52', 'Neck > chest'), ('75', 'Neck contra'), ('3', 'Neutral space'), ('2', 'Neutral space > head'), ('121', 'Neutral space > nose'), ('29', 'Neutral space/weak hand: front'), ('22', 'Nose'), ('103', 'Nose > chin'), ('122', 'Nose > neutral space'), ('116', 'Parallel plane'), ('125', 'R-loc'), ('126', 'R-loc > R-loc'), ('4', 'Shoulder'), ('153', 'Shoulder > chest'), ('115', 'Shoulder > shoulder'), ('123', 'Shoulder > weak hand: palm'), ('55', 'Shoulder contra'), ('131', 'Teeth'), ('146', 'Teeth'), ('43', 'Temple'), ('78', 'Temple > chest'), ('79', 'Thumb'), ('27', 'Tongue'), ('97', 'Trunk'), ('54', 'Upper arm'), ('63', 'Upper lip'), ('118', 'Variable'), ('91', 'Virtual object'), ('5', 'Weak hand'), ('6', 'Weak hand > arm'), ('11', 'Weak hand: back'), ('109', 'Weak hand: base'), ('66', 'Weak hand: finger tips'), ('210', 'Weak hand: fingers'), ('90', 'Weak hand: front'), ('96', 'Weak hand: index finger'), ('98', 'Weak hand: middle finger'), ('36', 'Weak hand: palm'), ('88', 'Weak hand: pinkie'), ('101', 'Weak hand: pinkie side'), ('99', 'Weak hand: ring finger'), ('139', 'Weak hand: thenar'), ('59', 'Weak hand: thumb'), ('100', 'Weak hand: thumb side'), ('111', 'Weak hand: thumb side > arm'), ('89', 'Weak hand: web space'), ('141', 'West'), ('50', 'Wrist')], default=0),
        ),
        migrations.AlterField(
            model_name='missingsignfeedback',
            name='smallmovement',
            field=models.IntegerField(blank=True, choices=[('0', '-'), ('1', 'N/A'), ('8', 'bent'), ('12', 'closed'), ('13', 'crossed'), ('5', 'curved'), ('3', 'extended'), ('9', 'flat'), ('11', 'flat-closed'), ('10', 'flat-open'), ('14', 'lax'), ('4', 'open')], default=0),
        ),
        migrations.AlterField(
            model_name='signfeedback',
            name='comment',
            field=models.TextField(blank=True, verbose_name='Comment or new keywords.'),
        ),
        migrations.AlterField(
            model_name='signfeedback',
            name='correct',
            field=models.IntegerField(choices=[(1, 'Yes'), (2, 'Mostly Correct'), (3, "Don't Know"), (4, 'Mostly Wrong'), (5, 'No'), (0, 'N/A')], verbose_name='Is the information about the sign correct?'),
        ),
        migrations.AlterField(
            model_name='signfeedback',
            name='isAuslan',
            field=models.IntegerField(choices=[(0, '---------'), (3, 'ASL'), (9, 'AdaSL'), (7, 'BISINDO'), (10, 'Berbey SL'), (4, 'CSL'), (11, 'IS'), (5, 'Kata Kolok'), (8, 'LSFB'), (12, 'LaSiMa'), (1, 'NGT'), (6, 'NTS'), (2, 'VGT')], verbose_name='Is this sign an Global Sign?'),
        ),
        migrations.AlterField(
            model_name='signfeedback',
            name='kwnotbelong',
            field=models.TextField(blank=True, verbose_name='List of keywords that DO NOT belong'),
        ),
        migrations.AlterField(
            model_name='signfeedback',
            name='like',
            field=models.IntegerField(choices=[(1, 'Morpheme'), (0, 'Sign')], verbose_name='Do you like this sign?'),
        ),
        migrations.AlterField(
            model_name='signfeedback',
            name='suggested',
            field=models.IntegerField(choices=[(1, 'Yes'), (2, 'Sometimes'), (3, "Don't Know"), (4, 'Perhaps'), (5, 'No'), (0, 'N/A')], default=3, verbose_name='If this sign is a suggested new sign, would you use it?'),
        ),
        migrations.AlterField(
            model_name='signfeedback',
            name='use',
            field=models.IntegerField(choices=[(1, 'Yes'), (2, 'Sometimes'), (3, 'Not Often'), (4, 'No'), (0, 'N/A')], verbose_name='Do you use this sign?'),
        ),
        migrations.AlterField(
            model_name='signfeedback',
            name='whereused',
            field=models.CharField(choices=[(0, (('n/a', 'N/A'),)), (1, (('1', 'Groningen'), ('2', 'Amsterdam'), ('3', 'Voorburg'), ('4', 'Rotterdam'), ('5', 'Gestel'), ('6', 'Unknown'))), (4, (('7', 'Beijing'), ('8', 'Shanghai'), ('9', 'Nanjing'), ('10', 'Unknown'))), (7, (('11', 'Ambon'), ('12', 'Makassar'), ('13', 'Padang'), ('14', 'Pontianak'), ('15', 'Singaradja'), ('16', 'Solo')))], max_length=10, verbose_name='Where is this sign used?'),
        ),
    ]
