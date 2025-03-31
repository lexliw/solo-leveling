
#%%
# lista dos capitulos que srão baixados -
mangaList = [
    "https://www.lermangas.com.br/2024/09/solo-leveling-capitulo-200.html",
    "https://www.lermangas.com.br/2024/09/solo-leveling-capitulo-199.html",
    "https://www.lermangas.com.br/2024/09/solo-leveling-capitulo-198.html",
    "https://www.lermangas.com.br/2024/09/solo-leveling-capitulo-197.html",
    "https://www.lermangas.com.br/2024/09/solo-leveling-capitulo-196.html",
    "https://www.lermangas.com.br/2024/09/solo-leveling-capitulo-195.html",
    "https://www.lermangas.com.br/2024/09/solo-leveling-capitulo-194.html",
    "https://www.lermangas.com.br/2024/09/solo-leveling-capitulo-193.html",
    "https://www.lermangas.com.br/2024/09/solo-leveling-capitulo-192.html",
    "https://www.lermangas.com.br/2024/09/solo-leveling-capitulo-191.html",
    "https://www.lermangas.com.br/2024/09/solo-leveling-capitulo-190.html",
    "https://www.lermangas.com.br/2024/09/solo-leveling-capitulo-189.html",
    "https://www.lermangas.com.br/2024/09/solo-leveling-capitulo-188.html",
    "https://www.lermangas.com.br/2024/09/solo-leveling-capitulo-187.html",
    "https://www.lermangas.com.br/2024/09/solo-leveling-capitulo-186.html",
    "https://www.lermangas.com.br/2024/09/solo-leveling-capitulo-185.html",
    "https://www.lermangas.com.br/2024/09/solo-leveling-capitulo-184.html",
    "https://www.lermangas.com.br/2024/09/solo-leveling-capitulo-183.html",
    "https://www.lermangas.com.br/2024/09/solo-leveling-capitulo-182.html",
    "https://www.lermangas.com.br/2024/09/solo-leveling-capitulo-181.html",
    "https://www.lermangas.com.br/2024/09/solo-leveling-capitulo-180.html",
    "https://www.lermangas.com.br/2024/09/solo-leveling-capitulo-179.html",
    "https://www.lermangas.com.br/2024/09/solo-leveling-capitulo-178.html",
    "https://www.lermangas.com.br/2024/09/solo-leveling-capitulo-177.html",
    "https://www.lermangas.com.br/2024/09/solo-leveling-capitulo-176.html",
    "https://www.lermangas.com.br/2024/09/solo-leveling-capitulo-175.html",
    "https://www.lermangas.com.br/2024/09/solo-leveling-capitulo-174.html",
    "https://www.lermangas.com.br/2024/09/solo-leveling-capitulo-173.html",
    "https://www.lermangas.com.br/2024/09/solo-leveling-capitulo-172.html",
    "https://www.lermangas.com.br/2024/09/solo-leveling-capitulo-171.html",
    "https://www.lermangas.com.br/2024/09/solo-leveling-capitulo-170.html",
    "https://www.lermangas.com.br/2024/09/solo-leveling-capitulo-169.html",
    "https://www.lermangas.com.br/2024/09/solo-leveling-capitulo-168.html",
    "https://www.lermangas.com.br/2024/09/solo-leveling-capitulo-167.html",
    "https://www.lermangas.com.br/2024/09/solo-leveling-capitulo-166.html",
    "https://www.lermangas.com.br/2024/09/solo-leveling-capitulo-165.html",
    "https://www.lermangas.com.br/2024/09/solo-leveling-capitulo-164.html",
    "https://www.lermangas.com.br/2024/09/solo-leveling-capitulo-163.html",
    "https://www.lermangas.com.br/2024/09/solo-leveling-capitulo-162.html",
    "https://www.lermangas.com.br/2024/09/solo-leveling-capitulo-161.html",
    "https://www.lermangas.com.br/2024/09/solo-leveling-capitulo-160.html",
    "https://www.lermangas.com.br/2024/09/solo-leveling-capitulo-159.html",
    "https://www.lermangas.com.br/2024/09/solo-leveling-capitulo-158.html",
    "https://www.lermangas.com.br/2024/09/solo-leveling-capitulo-157.html",
    "https://www.lermangas.com.br/2024/09/solo-leveling-capitulo-156.html",
    "https://www.lermangas.com.br/2024/09/solo-leveling-capitulo-155.html",
    "https://www.lermangas.com.br/2024/09/solo-leveling-capitulo-154.html",
    "https://www.lermangas.com.br/2024/09/solo-leveling-capitulo-153.html",
    "https://www.lermangas.com.br/2024/09/solo-leveling-capitulo-152.html",
    "https://www.lermangas.com.br/2024/09/solo-leveling-capitulo-151.html",
    "https://www.lermangas.com.br/2024/09/solo-leveling-capitulo-150.html",
    "https://www.lermangas.com.br/2024/09/solo-leveling-capitulo-149.html",
    "https://www.lermangas.com.br/2024/09/solo-leveling-capitulo-148.html",
    "https://www.lermangas.com.br/2024/09/solo-leveling-capitulo-147.html",
    "https://www.lermangas.com.br/2024/09/solo-leveling-capitulo-146.html",
    "https://www.lermangas.com.br/2024/09/solo-leveling-capitulo-145.html",
    "https://www.lermangas.com.br/2024/09/solo-leveling-capitulo-144.html",
    "https://www.lermangas.com.br/2024/09/solo-leveling-capitulo-143.html",
    "https://www.lermangas.com.br/2024/09/solo-leveling-capitulo-142.html",
    "https://www.lermangas.com.br/2024/09/solo-leveling-capitulo-141.html",
    "https://www.lermangas.com.br/2024/09/solo-leveling-capitulo-140.html",
    "https://www.lermangas.com.br/2024/09/solo-leveling-capitulo-139.html",
    "https://www.lermangas.com.br/2024/09/solo-leveling-capitulo-138.html",
    "https://www.lermangas.com.br/2024/09/solo-leveling-capitulo-137.html",
    "https://www.lermangas.com.br/2024/09/solo-leveling-capitulo-136.html",
    "https://www.lermangas.com.br/2024/09/solo-leveling-capitulo-135.html",
    "https://www.lermangas.com.br/2024/09/solo-leveling-capitulo-134.html",
    "https://www.lermangas.com.br/2024/09/solo-leveling-capitulo-133.html",
    "https://www.lermangas.com.br/2024/09/solo-leveling-capitulo-132.html",
    "https://www.lermangas.com.br/2024/09/solo-leveling-capitulo-131.html",
    "https://www.lermangas.com.br/2024/09/solo-leveling-capitulo-130.html",
    "https://www.lermangas.com.br/2024/09/solo-leveling-capitulo-129.html",
    "https://www.lermangas.com.br/2024/09/solo-leveling-capitulo-128.html",
    "https://www.lermangas.com.br/2024/09/solo-leveling-capitulo-127.html",
    "https://www.lermangas.com.br/2024/09/solo-leveling-capitulo-126.html",
    "https://www.lermangas.com.br/2024/09/solo-leveling-capitulo-125.html",
    "https://www.lermangas.com.br/2024/09/solo-leveling-capitulo-124.html",
    "https://www.lermangas.com.br/2024/09/solo-leveling-capitulo-123.html",
    "https://www.lermangas.com.br/2024/09/solo-leveling-capitulo-122.html",
    "https://www.lermangas.com.br/2024/09/solo-leveling-capitulo-121.html",
    "https://www.lermangas.com.br/2024/09/solo-leveling-capitulo-120.html",
    "https://www.lermangas.com.br/2024/09/solo-leveling-capitulo-119.html",
    "https://www.lermangas.com.br/2024/09/solo-leveling-capitulo-118.html",
    "https://www.lermangas.com.br/2024/09/solo-leveling-capitulo-117.html",
    "https://www.lermangas.com.br/2024/09/solo-leveling-capitulo-116.html",
    "https://www.lermangas.com.br/2024/09/solo-leveling-capitulo-115.html",
    "https://www.lermangas.com.br/2024/09/solo-leveling-capitulo-114.html",
    "https://www.lermangas.com.br/2024/09/solo-leveling-capitulo-113.html",
    # "https://www.lermangas.com.br/2024/09/solo-leveling-capitulo-112.html",
    # "https://www.lermangas.com.br/2024/09/solo-leveling-capitulo-111.html",
    # "https://www.lermangas.com.br/2024/09/solo-leveling-capitulo-110.html",
    # "https://www.lermangas.com.br/2024/09/solo-leveling-capitulo-109.html",
    # "https://www.lermangas.com.br/2024/09/solo-leveling-capitulo-108.html",
    # "https://www.lermangas.com.br/2024/09/solo-leveling-capitulo-107.html",
    # "https://www.lermangas.com.br/2024/09/solo-leveling-capitulo-106.html",
    # "https://www.lermangas.com.br/2024/09/solo-leveling-capitulo-105.html",
    # "https://www.lermangas.com.br/2024/09/solo-leveling-capitulo-104.html",
    # "https://www.lermangas.com.br/2024/09/solo-leveling-capitulo-103.html",
    # "https://www.lermangas.com.br/2024/09/solo-leveling-capitulo-102.html",
    # "https://www.lermangas.com.br/2024/09/solo-leveling-capitulo-101.html",
    # "https://www.lermangas.com.br/2024/09/solo-leveling-capitulo-100.html",
    # "https://www.lermangas.com.br/2024/09/solo-leveling-capitulo-99.html",
    # "https://www.lermangas.com.br/2024/09/solo-leveling-capitulo-98.html",
    # "https://www.lermangas.com.br/2024/09/solo-leveling-capitulo-97.html",
    # "https://www.lermangas.com.br/2024/09/solo-leveling-capitulo-96.html",
    # "https://www.lermangas.com.br/2024/09/solo-leveling-capitulo-95.html",
    # "https://www.lermangas.com.br/2024/09/solo-leveling-capitulo-94.html",
    # "https://www.lermangas.com.br/2024/09/solo-leveling-capitulo-93.html",
    # "https://www.lermangas.com.br/2024/09/solo-leveling-capitulo-92.html",
    # "https://www.lermangas.com.br/2024/09/solo-leveling-capitulo-91.html",
    # "https://www.lermangas.com.br/2024/09/solo-leveling-capitulo-90.html",
    # "https://www.lermangas.com.br/2024/09/solo-leveling-capitulo-89.html",
    # "https://www.lermangas.com.br/2024/09/solo-leveling-capitulo-88.html",
    # "https://www.lermangas.com.br/2024/09/solo-leveling-capitulo-87.html",
    # "https://www.lermangas.com.br/2024/09/solo-leveling-capitulo-86.html",
    # "https://www.lermangas.com.br/2024/09/solo-leveling-capitulo-85.html",
    # "https://www.lermangas.com.br/2024/09/solo-leveling-capitulo-84.html",
    # "https://www.lermangas.com.br/2024/09/solo-leveling-capitulo-83.html",
    # "https://www.lermangas.com.br/2024/09/solo-leveling-capitulo-82.html",
    # "https://www.lermangas.com.br/2024/09/solo-leveling-capitulo-81.html",
    # "https://www.lermangas.com.br/2024/09/solo-leveling-capitulo-80.html",
    # "https://www.lermangas.com.br/2024/09/solo-leveling-capitulo-79.html",
    # "https://www.lermangas.com.br/2024/09/solo-leveling-capitulo-78.html",
    # "https://www.lermangas.com.br/2024/09/solo-leveling-capitulo-77.html",
    # "https://www.lermangas.com.br/2024/09/solo-leveling-capitulo-76.html",
    # "https://www.lermangas.com.br/2024/09/solo-leveling-capitulo-75.html",
    # "https://www.lermangas.com.br/2024/09/solo-leveling-capitulo-74.html",
    # "https://www.lermangas.com.br/2024/09/solo-leveling-capitulo-73.html",
    # "https://www.lermangas.com.br/2024/09/solo-leveling-capitulo-72-const.html",
    # "https://www.lermangas.com.br/2024/09/solo-leveling-capitulo-71.html",
    # "https://www.lermangas.com.br/2024/09/solo-leveling-capitulo-70.html",
    # "https://www.lermangas.com.br/2024/09/solo-leveling-capitulo-69.html",
    # "https://www.lermangas.com.br/2024/09/solo-leveling-capitulo-68.html",
    # "https://www.lermangas.com.br/2024/09/solo-leveling-capitulo-67.html",
    # "https://www.lermangas.com.br/2024/09/solo-leveling-capitulo-66.html",
    # "https://www.lermangas.com.br/2024/09/solo-leveling-capitulo-65.html",
    # "https://www.lermangas.com.br/2024/09/solo-leveling-capitulo-64.html",
    # "https://www.lermangas.com.br/2024/09/solo-leveling-capitulo-63.html",
    # "https://www.lermangas.com.br/2024/09/solo-leveling-capitulo-62.html",
    # "https://www.lermangas.com.br/2024/09/solo-leveling-capitulo-61.html",
    # "https://www.lermangas.com.br/2024/09/solo-leveling-capitulo-60.html",
    # "https://www.lermangas.com.br/2024/09/solo-leveling-capitulo-59.html",
    # "https://www.lermangas.com.br/2024/09/solo-leveling-capitulo-58.html",
    # "https://www.lermangas.com.br/2024/09/solo-leveling-capitulo-57.html",
    # "https://www.lermangas.com.br/2024/09/solo-leveling-capitulo-56.html",
    # "https://www.lermangas.com.br/2024/09/solo-leveling-capitulo-55.html",
    # "https://www.lermangas.com.br/2024/09/solo-leveling-capitulo-54.html",
    # "https://www.lermangas.com.br/2024/09/solo-leveling-capitulo-53.html",
    # "https://www.lermangas.com.br/2024/09/solo-leveling-capitulo-52.html",
    # "https://www.lermangas.com.br/2024/09/solo-leveling-capitulo-51.html",
    # "https://www.lermangas.com.br/2024/09/solo-leveling-capitulo-50.html",
    # "https://www.lermangas.com.br/2024/09/solo-leveling-capitulo-49.html",
    # "https://www.lermangas.com.br/2024/09/solo-leveling-capitulo-48.html",
    # "https://www.lermangas.com.br/2024/09/solo-leveling-capitulo-47.html",
    # "https://www.lermangas.com.br/2024/09/solo-leveling-capitulo-46.html",
    # "https://www.lermangas.com.br/2024/09/solo-leveling-capitulo-45.html",
    # "https://www.lermangas.com.br/2024/09/solo-leveling-capitulo-44.html",
    # "https://www.lermangas.com.br/2024/09/solo-leveling-capitulo-43.html",
    # "https://www.lermangas.com.br/2024/09/solo-leveling-capitulo-42.html",
    # "https://www.lermangas.com.br/2024/09/solo-leveling-capitulo-41.html",
    # "https://www.lermangas.com.br/2024/09/solo-leveling-capitulo-40.html",
    # "https://www.lermangas.com.br/2024/09/solo-leveling-capitulo-39.html",
    # "https://www.lermangas.com.br/2024/09/solo-leveling-capitulo-38.html",
    # "https://www.lermangas.com.br/2024/09/solo-leveling-capitulo-37.html",
    # "https://www.lermangas.com.br/2024/09/solo-leveling-capitulo-36.html",
    # "https://www.lermangas.com.br/2024/09/solo-leveling-capitulo-35.html",
    # "https://www.lermangas.com.br/2024/09/solo-leveling-capitulo-34.html",
    # "https://www.lermangas.com.br/2024/09/solo-leveling-capitulo-33.html",
    # "https://www.lermangas.com.br/2024/09/solo-leveling-capitulo-32.html",
    # "https://www.lermangas.com.br/2024/09/solo-leveling-capitulo-31.html",
    # "https://www.lermangas.com.br/2024/09/solo-leveling-capitulo-30.html",
    # "https://www.lermangas.com.br/2024/09/solo-leveling-capitulo-29.html",
    # "https://www.lermangas.com.br/2024/09/solo-leveling-capitulo-28.html",
    # "https://www.lermangas.com.br/2024/09/solo-leveling-capitulo-27.html",
    # "https://www.lermangas.com.br/2024/09/solo-leveling-capitulo-26.html",
    # "https://www.lermangas.com.br/2024/09/solo-leveling-capitulo-25.html",
    # "https://www.lermangas.com.br/2024/09/solo-leveling-capitulo-24.html",
    # "https://www.lermangas.com.br/2024/09/solo-leveling-capitulo-23.html",
    # "https://www.lermangas.com.br/2024/09/solo-leveling-capitulo-22.html",
    # "https://www.lermangas.com.br/2024/09/solo-leveling-capitulo-21.html",
    # "https://www.lermangas.com.br/2024/09/solo-leveling-capitulo-20.html",
    # "https://www.lermangas.com.br/2024/09/solo-leveling-capitulo-19.html",
    # "https://www.lermangas.com.br/2024/09/solo-leveling-capitulo-18.html",
    # "https://www.lermangas.com.br/2024/09/solo-leveling-capitulo-17.html",
    # "https://www.lermangas.com.br/2024/09/solo-leveling-capitulo-16.html",
    # "https://www.lermangas.com.br/2024/09/solo-leveling-capitulo-15.html",
    # "https://www.lermangas.com.br/2024/09/solo-leveling-capitulo-14-const.html",
    # "https://www.lermangas.com.br/2024/09/solo-leveling-capitulo-13.html",
    # "https://www.lermangas.com.br/2024/09/solo-leveling-capitulo-12-const.html",
    # "https://www.lermangas.com.br/2024/09/solo-leveling-capitulo-11.html",
    # "https://www.lermangas.com.br/2024/09/solo-leveling-capitulo-10.html",
    # "https://www.lermangas.com.br/2024/09/solo-leveling-capitulo-9.html",
    # "https://www.lermangas.com.br/2024/09/solo-leveling-capitulo-8.html",
    # "https://www.lermangas.com.br/2024/09/solo-leveling-capitulo-7.html",
    # "https://www.lermangas.com.br/2024/09/solo-leveling-capitulo-6.html",
    # "https://www.lermangas.com.br/2024/09/solo-leveling-capitulo-5.html",
    # "https://www.lermangas.com.br/2024/09/solo-leveling-capitulo-4.html",
    # "https://www.lermangas.com.br/2024/09/solo-leveling-capitulo-3.html",
    # "https://www.lermangas.com.br/2024/09/solo-leveling-capitulo-2.html",
    # "https://www.lermangas.com.br/2024/09/solo-leveling-capitulo-1.html",
]
#%%
# funções que serão usadas para baixar os mangás
import requests
import os
def folderName(url):
    folder = url.split('/')[5].replace('.html','')
    num = folder.split('-')[3]
    znum = num.zfill(4)
    return folder.replace(f'-{num}',f'-{znum}')

def fileName(url):
    file = url.split('/')[3]
    num = file.split('-')[0]
    znum = num.zfill(4)
    result = file.replace(f'{num}-',f'{znum}-')
    if 'https://mangaonline.biz/wp-content/uploads/' in url:
        result = url.split('/')[7]
    # print(result)
    return result

def getManga(manga):
    url = manga
    folder = folderName(url)
    print(folder)

    # criar pasta
    newpath = f'./{folder}'
    if not os.path.exists(newpath):
        os.makedirs(newpath)
        # print('pasta criada')
    else:
        print('manga já baixado')
        return
    
    payload = {}
    headers = {}
    response = requests.request("GET", url, headers=headers, data=payload)

    imagesRaw = response.text.split("script>")
    # "https://mangaonline.biz/wp-content/uploads/2022/09/img_or04121905_0001.jpg",
    for chunk in imagesRaw:
        if 'https://meo.comick.pictures' in chunk or 'https://mangaonline.biz/wp-content/uploads/' in chunk:
            listRawImages = chunk.replace("const ts_reader = ", "").replace(";", "").replace("\n", "").replace("</", "").replace(" ", "")
            print(f'imagens: {listRawImages}')
        
    listImages = listRawImages.replace('["','').replace('",]','').replace('"]','').split('","')
    
    # baixar imagens
    for image in listImages:
        print(f'imagens: {image}')
        img_data = requests.get(image).content
        file = fileName(image)
        with open(f'./{folder}/{file}', 'wb') as handler:
            handler.write(img_data)

    # return listImages
#%%
# lista = getManga('https://www.lermangas.com.br/2024/09/solo-leveling-capitulo-96.html')
#%%
# loop para baixar os mangás
for manga in mangaList:
    getManga(manga)

# print(response.text) "https://meo.comick.pictures/1-Pt0kp13YjAfKd.jpg",

# %%
# listar o nome das imagens
from os import listdir
from os.path import isfile, isdir, join

mypath = './'

onlyfolders = [f for f in listdir(mypath) if isdir(join(mypath, f))]
onlyfolders.sort()
onlyfolders.remove('.git')
print(onlyfolders)

for folder in onlyfolders:
    chapterFolder = f'./{folder}/'
    onlyfiles = [f for f in listdir(chapterFolder) if isfile(join(chapterFolder, f))]
    onlyfiles.sort()
    print(f'{folder}:{onlyfiles}')
# %%
# trata o nome das imagens
from os import listdir
from os.path import isfile, isdir, join

mypath = './'

onlyfolders = [f for f in listdir(mypath) if isdir(join(mypath, f))]
onlyfolders.sort()
onlyfolders.remove('.git')
print(onlyfolders)

for folder in onlyfolders:
    chapterFolder = f'./{folder}/'
    onlyfiles = [f for f in listdir(chapterFolder) if isfile(join(chapterFolder, f))]
    onlyfiles.sort()
    for file in onlyfiles:
        if '_' in file :
            newfilename= file.replace('_','x')        
            print(f'{folder}: {file} -> {newfilename}')
            os.rename(f'{chapterFolder}{file}', f'{chapterFolder}{newfilename}')
    
    onlyfiles = [f for f in listdir(chapterFolder) if isfile(join(chapterFolder, f))]
    onlyfiles.sort()
    print(f'{folder}:{onlyfiles}')


# %%
# cria os readme.md
from os import listdir
from os.path import isfile, isdir, join

mypath = './'

onlyfolders = [f for f in listdir(mypath) if isdir(join(mypath, f))]
onlyfolders.sort()
onlyfolders.remove('.git')
print(onlyfolders)

conteudo = '# Solo Leveling\n'
for folder in onlyfolders:
    #- [teste](/chap-0001/readme.md)
    conteudo += f'- [{folder}](/{folder}/readme.md)\n'
    # conteudo += f'<p style="text-align: center;"><button name="menu" onclick="/{folder}/readme.md">{folder}</button></p>'


print('./readme.md')
f = open('./readme.md', 'w')
f.write(conteudo)
f.close()

for i in range(len(onlyfolders)):
    chapterFolder = f'./{onlyfolders[i]}/'
    anterior = '/solo-leveling/'
    proximo = '/solo-leveling/'
    menu = '/solo-leveling/'
    if i - 1 >= 0: 
        anterior = f'/solo-leveling/{onlyfolders[i-1]}/'
    if i + 1 <= len(onlyfolders)-1: 
        proximo = f'/solo-leveling/{onlyfolders[i+1]}/'

    onlyfiles = [f for f in listdir(chapterFolder) if isfile(join(chapterFolder, f))]
    onlyfiles.sort()
    if 'readme.md' in onlyfiles:
        onlyfiles.remove('readme.md')
    # print(f'{onlyfolders[i]}:{onlyfiles}')
    navegacao = f'##### [ANTERIOR]({anterior})&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[MENU]({menu})&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[PRÓXIMO]({proximo})\n'
    conteudo = f'# {onlyfolders[i]}\n{navegacao}'

    for file in onlyfiles:
        conteudo += f'![{file}]({file})\n\n'
    
    conteudo += f'{navegacao}'

    print(f'{chapterFolder}readme.md')
    f = open(f'{chapterFolder}readme.md', 'w')
    f.write(conteudo)
    f.close()

# %%
