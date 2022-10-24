# -*- coding: utf-8 -*-
###############################################################################
#
#    Tech-Receptives Solutions Pvt. Ltd.
#    Copyright (C) 2009-TODAY Tech-Receptives(<http://www.techreceptives.com>).
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
###############################################################################

{
    'name': 'OpenEduCat Core',
    'version': '1.2.0',
    'category': 'Openerp Education',
    "sequence": 3,
    'summary': 'Manage Students, Faculties and Education Institute',
    'complexity': "easy",
    'description': """
        This module provide core education management system over OpenERP
        Features includes managing
            * Student
            * Faculty
            * Course
            * Batch

    """,
    'author': 'Tech Receptives',
    'website': 'http://www.openeducat.org',
    'depends': ['document', 'hr', 'web', 'website'],
    'data': [
        'security/op_security.xml',
        'security/ir.model.access.csv',
        'views/student_view.xml',
        'views/course_view.xml',
        'views/batch_view.xml',
        'views/subject_view.xml',
        'views/roll_number_view.xml',
        'views/faculty_view.xml',
        'views/res_company_view.xml',
        'views/openeducat_template.xml',
        'views/homepage_template.xml',
        'menu/openeducat_core_menu.xml',
        'menu/student_menu.xml',
        'menu/faculty_menu.xml'
    ],
    'demo': [
        'demo/op.course.csv',
        'demo/op.batch.csv',
        'demo/res.users.csv',
        'demo/op.student.csv',
        'demo/op.faculty.csv',
        'demo/op.subject.csv',
        'demo/res.groups.csv'
    ],
    'css': ['static/src/css/base.css'],
    'qweb': [
        'static/src/xml/base.xml'],
    'js': ['static/src/js/chrome.js'],
    'installable': True,
    'auto_install': False,
    'application': True,
}


# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
