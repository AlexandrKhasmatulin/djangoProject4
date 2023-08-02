from django.contrib import admin

from send_emails.models import Mailing, SmsLetter, MailingLog, Client


admin.site.register(Mailing)
admin.site.register(Client)
admin.site.register(MailingLog)
admin.site.register(SmsLetter)
