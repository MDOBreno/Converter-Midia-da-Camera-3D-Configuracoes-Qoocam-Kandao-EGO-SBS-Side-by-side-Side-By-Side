---------------------- Instruções para converter Fotos e Videos -----------------------

[Introdução]
	- O intuito é converter as fotos e videos da camera 3D "Kandao QooCam EGO", 
	que na teoria cada quadro são duas imagens(olho esquerdo e direito)
	mescladas lado-a-lado de resolução e proporção FullHD para cada olho, 
	em que na pratica é o seguinte:
	 	[Foto]:  8000×3000 pixels
	 	[Video]: 3840×1080 pixels

	- Então o que queremos é gerar 4 tipos de arquivos e deletar os 
	originais mencionados acima, os quais são:
		[Foto 	- Spatial Photo(.heic)]: 	4000×3000 pixels
		[Video 	- Spatial Video(.mov)]: 	1920x1080 pixels
		[Foto 	- SBS 16x9(.jpg)]: 			8000x4500 pixels
		[Video 	- SBS 16x9(.m4v)]: 			4K(3840x2160 pixels)

	- Todas as conversões acima, tanto pra foto quanto pra video,
	devem ser feitos diretamente da respectiva foto/video original
	- As instruções são semanticamente "divididas em 3 partes":
		- Converter [Foto/Video pra Spatial Photo/Video]: Instruções exigem Mac(Apple)
		- Converter [Foto pra SBS]:  Instruções exigem Mac(Apple ou Intel)
		- Converter [Video pra SBS]: Instruções exigem Mac(Apple ou Intel)
		- Ajustar Data/Hora automaticamente: Mac(Apple ou Intel) ou Windows
		- Preencher localização da foto: Instruções exigem Mac(Apple ou Intel)
	as 3 primeiras de "Converter" podem ser feitas independentemente entre si,
	mas qualquer uma delas exige as duas ultimas ("Ajustar Data/Hora e "Preencher 
	localização")
	- Os resultados são a forma mais eficiente, em todos os quesitos:
		--> Adicao minima possível de redundancia de pixels afim de se obter a 
		proporção padrão de mercado: 16x9
		--> Conversão para formatos mais eficientes(leitura e Armazenamento minimo)
		de arquivos SBS e Spatial(da Apple) de arquivos de midia 3D na proporção 
		padrão de mercado: 16x9
	- Para cada um um dos 4 tipos de arquivo de destino, siga a instrução abaixo.
	- Uma dica: Se você tiver um servidor NAS faça todo o tratamento diretamente nele,
    pois em varias etapas esses arquivos(que já são pesados) são duplicados,
    comprometendo o armazenamento interno, e atrapalhando um possível 
    Swap de Memoria caso algum processamento exija mais memoria ram do que a 
    maquina possua. Além de que velocidades de HDs(geralmente instalados em NASs, e
    operando a 100MB/s), conseguem ser mais rapidos do que a velocidade de encode
    do video, o que torna irrelevante usar o SSD interno ou um HD para esse proposito.
    	

_______________________________________________________________________________________

[Foto - Spatial Photo(.heic)] e [Video - Spatial Video(.mov)]
	- Entre na pasta:
		"SpatialConverter-vX.X.X"
	- Abra o arquivo/site "WebPage Download Releases"
	- Se no site tiver uma versão mais recente, baixar/substituir(por)/usar ela
	- Dentro da pasta "SpatialConverter-vX.X.X", execute o README.txt
    - Pra ajustar a dataHora dessas fotos/videos, faça o procedimento abaixo chamado:
    	[Ajustar Data/Hora automaticamente(Obrigatorio)]
	- Em seguida arraste tais arquivos para seu App "Fotos (do iCloud), e ele 
	começará a importar e sicronizar essa midia com a nuvem iCloud.
	- Quando a sincronização for concluida faça o seguinte: Para cada conjunto de 
	fotos/videos batidas no mesmo local, selecione todos, depois "Command+i", 
	click no nome da localização, escreva/busque pelo nome/endereço do local, 
	e de enter.

_______________________________________________________________________________________

[Foto - SBS 16x9(.jpg)]
	- A ideia aqui é amplicar(redundancia de pixel) as fotos afim de alcançar a 
	proporção padrão 16x9 das Tvs/Monitores, conforme arquivo "Proporcoes e Pixels.png"
	- Duplique a pasta das fotos originais{[Foto]: 8000×3000 pixels}, 
	pois este procedimento altera os arquivos(em vez de criar/exportar novos arquivos)
	no formato desejado, o que impediria de: 
		- Fazer as demais conversões desse tutorial
		- Ter um backup para o caso de algum problema ocorrer.
	- Selecione todos, e de um [Command+o] para abrir todos em uma janela do
	Aplicativo Preview(pre-visualização) nativo do MacOS
	- Click em uma foto da lista lateral, [Command+A] para selecionar todas as fotos
	- Click em: Ferramentas -> AjustarTamanho
	- Click no Cadeado para abri-lo, e em altura coloca 4500pixels, e clica em OK
	- Click em uma foto da lista, [Command+A] para selecionar todos
	- [Command+S] para salvar todos
    - Pra ajustar a dataHora dessas fotos/videos, faça o procedimento abaixo chamado:
    	[Ajustar Data/Hora automaticamente(Obrigatorio)]
	- Em seguida arraste tais arquivos para seu App "Fotos (do iCloud), e ele 
	começará a importar e sicronizar essa midia com a nuvem iCloud.
	- Quando a sincronização for concluida faça o seguinte: Para cada conjunto de 
	fotos/videos batidas no mesmo local, selecione todos, depois "Command+i", 
	click no nome da localização, escreva/busque pelo nome/endereço do local, 
	e de enter.

_______________________________________________________________________________________

[Video - SBS 16x9(.m4v)]
	- A ideia aqui é amplicar(redundancia de pixel) as fotos afim de alcançar a 
	proporção padrão 16x9 das Tvs/Monitores, conforme arquivo "Proporcoes e Pixels.png"
	- Gere os arquivos seguindo as instruções em constam em:
	"/Video/Instrucoes no FinalCutPro.pdf"
	- O ato de abrir o video depois de exportar gera CopiasDuplicadas, eu não sei o
	porque disso ocorrer, na seguinte pasta(então é bom deletar para liberar espaço, 
	Ex: 50GB):
		'/Users/SeuUsuarioDoMac/Movies/TV/Media.localized/Home Videos'
    - Pra ajustar a dataHora dessas fotos/videos, faça o procedimento abaixo chamado:
    	[Ajustar Data/Hora automaticamente(Obrigatorio)]
	- Em seguida arraste tais arquivos para seu App "Fotos (do iCloud), e ele 
	começará a importar e sicronizar essa midia com a nuvem iCloud.
	- Quando a sincronização for concluida faça o seguinte: Para cada conjunto de 
	fotos/videos batidas no mesmo local, selecione todos, depois "Command+i", 
	click no nome da localização, escreva/busque pelo nome/endereço do local, 
	e de enter.
        
_______________________________________________________________________________________

[Ajustar Data/Hora automaticamente(Obrigatorio)]
	- Se você não tiver instalado na sua maquina o exiftool, instale assim:
		- No MacOS (assumindo que você já tem o gerenciador de pacotes HomeBrew):
			brew install exiftool
		- No Windows (assumindo que você já tem o gerenciador de pacotes Chocolatey):
			choco install exiftool
	- Agora vá na sua câmera, abra: Settings -> "Date & Time" -> "Time Zone"
	e anote a fuso horário que está configurado lá. (No meu caso está -3:00)
	- Para corrigir as data/horas na pasta ExecutavelDeScriptDeCorrecaoDeDataHora
	existe um arquivo chamado gerar_scripts.py, e na linha 19, que contem o conteudo:
		[ if add_timezone: 					]
	    [ 	dt -= timedelta(hours=-3)   	]
	substitua o valor "-3" pelo valor que aparecia na sua camera em "Time Zone"
	quando você capturou suas fotos e videos, que no meu exemplo devo manter "-3"
	- Em seguida faça uma copia do arquivo gerar_scripts.py para a pasta que contem
    esses arquivos, e execute no teminal:
    	python3 gerar_scripts.py
    Isso cria os executaveis corrigir_datas.sh(Mac) e corrigir_datas.bat(Windows)
    Então faça o seguinte pro seu sistema operacional:
    	--> Windows: 		(Dois clicks no corrigir_datas.bat)
		--> Mac(teminal): 	./corrigir_datas.sh
	Isso vai ajeitar as datas automaticamente.
	- Repare que os arquivos [Spatial Photo/Video], por ser moderno/versatil eu
	uso como padrão na data/Hora exata que ocorreu, mas deixo o [Photo/Video - SBS]
	com a data/Hora exata porém com 100 anos antes, para estar no mesmo album 
	(porém separado no tempo) de forma que eu consiga assistir 
	sequencialmente/facilmente na TV 3D, e ao mesmo tempo eu consiga entender
	facilmente o momento da foto.

