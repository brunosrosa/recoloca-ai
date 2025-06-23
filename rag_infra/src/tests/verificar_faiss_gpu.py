import torch
import faiss
import numpy as np

print("--- Verificação do PyTorch ---")
print(f"Versão do PyTorch: {torch.__version__}")
pytorch_cuda_disponivel = torch.cuda.is_available()
print(f"PyTorch CUDA disponível: {pytorch_cuda_disponivel}")

if pytorch_cuda_disponivel:
    print(f"Versão do CUDA que o PyTorch está usando: {torch.version.cuda}")
    print(f"Nome da GPU detectada pelo PyTorch: {torch.cuda.get_device_name(0)}")
    print(f"Número de GPUs detectadas pelo PyTorch: {torch.cuda.device_count()}")
else:
    print("PyTorch não conseguiu encontrar uma GPU compatível com CUDA.")

print("\n--- Verificação do FAISS ---")
print(f"Versão do FAISS: {faiss.__version__}")

try:
    num_gpus_faiss = faiss.get_num_gpus()
    print(f"Número de GPUs que o FAISS detecta: {num_gpus_faiss}")

    if num_gpus_faiss > 0:
        print("FAISS GPU parece estar ATIVO e detectou GPUs.")

        # Teste mais aprofundado de criação e uso de índice na GPU
        dimensao = 128  # Dimensão dos vetores de exemplo
        num_vetores_base = 1000
        num_vetores_consulta = 100
        k_vizinhos = 5

        print(f"\nTentando criar um índice GpuIndexFlatL2 na GPU 0 com dimensão {dimensao}...")

        # 1. Alocar recursos da GPU
        try:
            recursos_gpu = faiss.StandardGpuResources()
            print("Recursos da GPU (StandardGpuResources) alocados com sucesso.")
        except Exception as e_res:
            print(f"ERRO ao alocar StandardGpuResources: {e_res}")
            print("Isso pode indicar um problema com a comunicação com a GPU ou drivers.")
            exit()

        # 2. Configurar e criar o índice na GPU
        try:
            config_indice_gpu = faiss.GpuIndexFlatConfig()
            config_indice_gpu.device = 0 # Usar a GPU 0
            indice_gpu = faiss.GpuIndexFlatL2(recursos_gpu, dimensao, config_indice_gpu)
            print(f"Índice GpuIndexFlatL2 criado na GPU. Treinado: {indice_gpu.is_trained}, Total de vetores: {indice_gpu.ntotal}")
        except Exception as e_idx:
            print(f"ERRO ao criar GpuIndexFlatL2: {e_idx}")
            print("Verifique a compatibilidade do FAISS com sua versão do CUDA e drivers.")
            exit()

        # 3. Adicionar vetores ao índice
        try:
            np.random.seed(42) # Para reprodutibilidade
            vetores_base = np.random.random((num_vetores_base, dimensao)).astype('float32')
            indice_gpu.add(vetores_base)
            print(f"Adicionados {indice_gpu.ntotal} vetores ao índice na GPU.")
        except Exception as e_add:
            print(f"ERRO ao adicionar vetores ao índice GPU: {e_add}")
            exit()

        # 4. Realizar uma busca
        try:
            vetores_consulta = np.random.random((num_vetores_consulta, dimensao)).astype('float32')
            distancias, indices = indice_gpu.search(vetores_consulta, k_vizinhos)
            print(f"Busca realizada com sucesso na GPU. Shape das distâncias: {distancias.shape}, Shape dos índices: {indices.shape}")
            print("Exemplo dos primeiros 5 vizinhos para a primeira consulta:")
            print(f"  Índices: {indices}")
            print(f"  Distâncias: {distancias}")
            print("\nVERIFICAÇÃO DO FAISS-GPU CONCLUÍDA COM SUCESSO!")
        except Exception as e_search:
            print(f"ERRO ao realizar busca no índice GPU: {e_search}")
            exit()

    else:
        print("FAISS GPU NÃO está ativo ou não detectou GPUs.")
        print("FAISS pode estar operando em modo CPU apenas.")
        # Tentar importar um índice CPU para ver se o FAISS base funciona
        try:
            indice_cpu = faiss.IndexFlatL2(128)
            print("FAISS CPU (IndexFlatL2) importado e criado com sucesso.")
        except Exception as e_cpu:
            print(f"Falha ao criar índice FAISS CPU: {e_cpu}")

except AttributeError as e_attr:
    print(f"ERRO de Atributo no FAISS: {e_attr}")
    print("Isso pode significar que o pacote 'faiss-gpu' não foi instalado corretamente,")
    print("ou que uma versão apenas CPU ('faiss-cpu') está instalada e ativa.")
    print("Verifique se você instalou 'faiss-gpu' e não 'faiss-cpu' se deseja suporte a GPU.")
except Exception as e_geral:
    print(f"Um erro inesperado ocorreu durante a verificação do FAISS: {e_geral}")
