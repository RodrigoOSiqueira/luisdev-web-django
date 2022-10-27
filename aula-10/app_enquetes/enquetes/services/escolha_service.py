from ..models import Escolha


class EscolhaService:
    def __init__(self, escolha_id: int) -> None:
        self._escolha_id = escolha_id


    def vote(self) -> Escolha:
        """
        Atualizando a escolha utilizando o filter
        Escolha.objects.filter(id=self._escolha_id).update(texto="Texto novo")

        """
        escolha = Escolha.objects.get(id=self._escolha_id)
        escolha.num_votos += 1
        escolha.save()
        
        return escolha
