from service_objects.services import Service

from transportation.models import StationModel


class StationsContextDataService(Service):

	def process(self):
		return {'stations': self.get_stantions}

	@property
	def get_stantions(self):
		return StationModel.objects.all()
