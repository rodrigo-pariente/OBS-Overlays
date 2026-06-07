# OBS Overlays

Um sistema de overlays para o OBS baseado em widgets, design consistente e integração com a twitch.

<p align="center">
    <img src="https://github.com/rodrigo-pariente/obs-overlays/blob/main/img/demo.jpg" alt="Lindos overlays similares a janelas GTK" width="450">
</p>


## O Que Esse Repositório Contém?

- Widgets para **Chat**, **Follow** e outras integrações com a Twitch

- Widgets utilitários como **Balão de Siga-Me** temporizado e widget de objetivos.

> [!INFO]
> A API da twitch é consumida através de clientes montados com auxílio da biblioteca <a href="https://pytwitchapi.dev/en/stable/">`pythonTwitchAPI`</a>


## Como Usar

A partir do diretorio base, execute o script de configuração dos ambientes virtuais

`$ .scripts/setup-environment.sh`

Ative o Bot de leitura do Chat com

`$ .scripts/run-twitch-bot.sh`

Ative a inscrição de eventos da Twitch com

`$ .scripts/run-twitch-follow.sh`

Ative o servidor web de Widgets com

`$ .scripts/run-widgets.sh`

Acesse `localhost:5000` e veja os widgets disponíveis. É possível usá-los como qualquer outro overlay de OBS.

> [!IMPORTANT]
> Este repositório depende em python3 e bash e foi projetado para rodar em ambiente UNIX-like.


## Como Configurar

### Twitch API

Para widgets que dependem da API fornecida pela Twitch, é necessário ter uma Aplicação de Desenvolvedor.

Facilmente é possível obter estas informações seguindo os passos em <a href="https://www.educative.io/courses/channels-video-twitch-api-python/get-started">twitch-api-tutorial</a> e usar a URL de redirecionamento fornecida pela library twitchAPI `http://localhost:17563`.

Insira o ID e Segredo da aplicação cliente no json em `commons/twitch_app.json`. Os widgets devem estar prontos para receber informações do canal!
