from odoo import fields,models

class helpdesk_ticket(models.Model):
   _name = "helpdek.ticket"
   _description = "Helpdesk Ticket"

   name = fields.Char()
   description = fields.Text()
   date = fields.Date(help="Date when the ticket was created")
   limit_date = fields.Datetime(help="Date and time when the tcket will be closed")
   assigned = fields.Boolean(help="Ticket assigned to someone")
   acctions_todo = fields.Html()



