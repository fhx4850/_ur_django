
class Edit:
    def __init__(self, request, update_model_instance):
        self._model = update_model_instance
        self._form_data = request.POST | request.FILES
        self._all_model_fields = self._model._meta.get_fields(include_parents=False)
        self._model_fields = self._extract_fields()
        self._update()

    def _extract_fields(self):
        fields = list()
        for field in self._all_model_fields:
            try:
                fields.append(field.get_attname())
            except:
                pass
        return fields

    def _update(self):
        print(self._form_data['pm_avatar'])
        for i in self._form_data:
            if i in self._model_fields:
                print(i)