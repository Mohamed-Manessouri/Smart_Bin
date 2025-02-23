from torchvision.datasets import ImageFolder
import torchvision.transforms as transforms
import os 


# Awal haja hia nakhdo data so ghanst3mlo os library bach n retrieviw classes mn dir li kayna fl path
path = 'C:/Users/moham/Dokument/Club/Formation/Smart_Bin/dataset/GarbageClassification'

classes = os.listdir(path)

print(classes)



#tani haja khas ga3 tsawr ykouno b le même format w moraha nrj3ohom tensors(vectors) bach model y9dr ytrini 3la des valeur num)

transformations = transforms.Compose([transforms.Resize((256, 256)), transforms.ToTensor()])

dataset = ImageFolder(path, transform = transformations)

print(f"Total images in the dataset: {len(dataset)}")
