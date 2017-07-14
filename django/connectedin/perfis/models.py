from django.db import models

class Perfil(models.Model):

    name = models.CharField(max_length=255, null=False)
    email = models.CharField(max_length=255,null=False)
    job = models.CharField(max_length=255,null=False, default='undefined')
    phone_number = models.CharField(max_length=15, null=False)
    company_name = models.CharField(max_length=255, null=False)
    contacts = models.ManyToManyField('self')

    def to_invite(self, perfil_invited):
        Invite(requester=self, invited=perfil_invited).save()


class Invite(models.Model):

    requester = models.ForeignKey(Perfil, related_name='invite_sent')
    invited =  models.ForeignKey(Perfil, related_name='invite_received')

    def accept(self):
        self.invited.contacts.add(self.requester)
        self.requester.contacts.add(self.invited)
        self.delete()


