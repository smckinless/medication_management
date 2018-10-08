from rest_framework import views, generics, status
from rest_framework.response import Response
from medication_management.models import Medication, Patient
from medication_management.serializers import MedicationSerializer, PatientSerializer


class MedicationAPI(generics.CreateAPIView):
    """
    Endpoint to create a Medication.
    """
    queryset = Medication.objects.all()
    serializer_class = MedicationSerializer


class PatientAPI(generics.CreateAPIView):
    """
    Endpoint to create a Patient.
    """
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer


class AddPatientMedicationAPI(views.APIView):
    """
    Endpoint to add a medication to a patient.
    """
    def post(self, request, patient_id):
        medication_id = request.POST['id']
        try:
            medication = Medication.objects.get(id=medication_id)
        except Medication.DoesNotExist:
            medication = None
        try:
            patient = Patient.objects.get(id=patient_id)
        except Patient.DoesNotExist:
            patient = None

        if medication and patient and medication not in patient.medications.all():
            patient.medications.add(medication)
            patient.save()
            return Response({"Medication added"}, status=status.HTTP_200_OK)

        return Response({"Could not add medication to patient"}, status=status.HTTP_400_BAD_REQUEST)


class RemovePatientMedicationAPI(views.APIView):
    """
    Endpoint to remove a medication from a patient.
    """
    def post(self, request, patient_id):
        medication_id = request.POST['id']
        try:
            medication = Medication.objects.get(id=medication_id)
        except Medication.DoesNotExist:
            medication = None
        try:
            patient = Patient.objects.get(id=patient_id)
        except Patient.DoesNotExist:
            patient = None

        if medication and patient and medication in patient.medications.all():
            patient.medications.remove(medication)
            patient.save()
            return Response({"Medication removed"}, status=status.HTTP_200_OK)

        return Response({"Could not remove medication from patient"}, status=status.HTTP_400_BAD_REQUEST)