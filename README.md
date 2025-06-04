--------------------- Instruções para converter Fotos e Videos----------------------

[Introdução]
	- O intuito é converter as fotos e videos da camera 3D, 
	que na teoria cada quadro são duas imagens(olho esquerdo e direito)
	mescladas lado-a-lado de resolução e proporção FullHD cada olho, 
	em que na pratica é p seguinte:
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

	- Os resultados são a forma mais eficiente, em todos os quesitos:
		--> Adicao minima possível de redundancia de pixels
		--> Conversão para formatos mais eficientes(leitura e Armazenamento minimo)

	- Para cada um um dos 4 tipos de arquivo de destino, siga a instrução abaixo:

____________________________________________________________________________________

[Foto - Spatial Photo(.heic)] e [Video - Spatial Video(.mov)]
	- Entre na pasta:
		"SpatialConverter-vX.X.X"
	- Abra o arquivo/site "WebPage Download Releases"
	- Se no site tiver uma versão mais recente, baixar/substituir(por)/usar ela
	- Dentro da pasta "SpatialConverter-vX.X.X", execute o README.txt
	- Coloque os arquivos gerados no App Fotos, depois "Command+i",
		e duploClick para atualizar dataHora e localização.
		Ex: "0034_20250110_142609_01.mp4" colocar 10/01/2025 14:26:09
	- A cada conjunto de fotos/videos batidas no mesmo local, selecione todos,
		 depois "Command+i", clique no nome da localização, 
		 escreva/busque pelo nome/endereço do local, e de enter.

____________________________________________________________________________________

[Foto - SBS 16x9(.jpg)]
	- A ideia aqui é amplicar(redundancia de pixel) as fotos afim de alcançar a 
		proporção padrão 16x9 das Tvs/Monitores, conforme arquivo em:
		"/Fotos/Proporcoes e Pixels.png"
	- Duplique a pasta das fotos originais{[Foto]: 8000×3000 pixels}, 
		pois vamos alterar os arquivos em vez de usar um programa que
		cria/exporta novos arquivos no formato desejado.
	- Selecione todos, e de um [Command+o] para abrir todos em uma janela do
		Aplicativo Preview(pre-visualização) nativo do MacOS
	- Clique em uma foto da lista, [Command+A] para selecionar todos
	- Click em: Ferramentas -> AjustarTamanho
	- Click no Cadeado para abri-lo, e em altura coloca 4500pixels, e clica em OK
	- Clique em uma foto da lista, [Command+A] para selecionar todos
	- [Command+S] para salvar todos
	- Coloque os arquivos gerados no App Fotos, depois "Command+i",
		e duploClick para atualizar dataHora(MENOS 100 ANOS) e localização.
		Ex: "0034_20250110_142609_01.mp4" colocar 10/01/1925 14:26:09
	- A cada conjunto de fotos/videos batidas no mesmo local, selecione todos,
		 depois "Command+i", clique no nome da localização, 
		 escreva/busque pelo nome/endereço do local, e de enter.

____________________________________________________________________________________

[Video - SBS 16x9(.m4v)]
	- A ideia aqui é amplicar(redundancia de pixel) os videos afim de alcançar a 
		proporção padrão 16x9 das Tvs/Monitores, conforme arquivo em:
		"/Fotos/Proporcoes e Pixels.png"
	- Gere os arquivos com as instruções em constam em:
		"/Video/Instrucoes no FinalCutPro.pdf"
	- Coloque os arquivos gerados no App Fotos, depois "Command+i",
		e duploClick para atualizar dataHora(MENOS 100 ANOS) e localização.
		Ex: "0034_20250110_142609_01.mp4" colocar 10/01/1925 14:26:09
	- A cada conjunto de fotos/videos batidas no mesmo local, selecione todos,
		 depois "Command+i", clique no nome da localização, 
		 escreva/busque pelo nome/endereço do local, e de enter.

____________________________________________________________________________________



