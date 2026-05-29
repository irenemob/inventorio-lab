# Dados do inventário físico
reagentes = ['Etanol', 'Acetona', 'Etanol', 'Ácido Sulfúrico', 'Benzeno', 'Acetona',
             'Etanol', 'Ácido Sulfúrico', 'Metanol', 'Tolueno', 'Etanol', 'Acetona',
             'Ácido Acético', 'Etanol', 'Benzeno', 'Ácido Sulfúrico', 'Metanol',
             'Ácido Acético', 'Etanol', 'Acetona', 'Tolueno', 'Ácido Sulfúrico',
             'Benzeno', 'Etanol', 'Acetona', 'Metanol', 'Ácido Sulfúrico', 'Acetona',
             'Ácido Acético', 'Etanol']

lotes = ['2023-ETA-01', '2023-ACE-01', '2023-ETA-01', '2023-SUL-01', '2023-BEN-01',
         '2024-ACE-01', '2023-ETA-02', '2024-SUL-01', '2023-MET-01', '2024-TOL-01',
         '2023-ETA-01', '2023-ACE-01', '2023-ACA-01', '2023-ETA-02', '2023-BEN-01',
         '2023-SUL-01', '2023-MET-01', '2024-ACA-01', '2023-ETA-01', '2023-ACE-01',
         '2024-TOL-01', '2024-SUL-01', '2023-BEN-01', '2023-ETA-01', '2023-ACE-01',
         '2023-MET-01', '2023-SUL-01', '2024-ACE-01', '2024-ACA-01', '2023-ETA-02']

purezas = [99.5, 92.0, 99.5, 98.0, 99.9, 98.5, 96.0, 99.0, 99.0, 98.8, 99.5, 92.0,
           99.2, 96.0, 99.9, 98.0, 99.0, 95.0, 99.5, 92.0, 98.8, 99.0, 99.9, 99.5,
           92.0, 99.0, 98.0, 98.5, 95.0, 96.0]

#identificando e contando os tipos de reagentes
tipos_reagentes = set(reagentes)
quantidade_reagentes = len(tipos_reagentes)

inventario = list(zip(reagentes, lotes, purezas))

#print inicial 
print('=' * 90)
print('                     RELATÓRIO DO ESTOQUE DO LABORATÓRIO')
print('=' * 90)
print(f'\n >Há {quantidade_reagentes} tipos de reagentes diferentes no laboratório.')
print(f' >São eles: {tipos_reagentes}\n')
print('=' * 90)
print('                     LISTA DOS REAGENTES INDIVIDUAIS:')
print('=' * 90)
print('\n')

#loop exigido 
for reagente, lote, pureza in inventario:
    print(f'Frasco do Lote: [{lote}] | Reagente: [{reagente}] | Pureza: [{pureza}]%\n')

#print do loop
print('=' * 90)
print('           LOTES APROVADOS PARA EXPERIMENTOS SENSÍVEIS (pureza >= 98%)')
print('=' * 90)

lotes_aprovados = [lote for reagente, lote, pureza in inventario if pureza >= 98.0]

print(f'\n >Dos lotes anteriores, {len(lotes_aprovados)} foram aprovados. ')
print(f'\n >Os códigos aprovados são: {lotes_aprovados} \n')