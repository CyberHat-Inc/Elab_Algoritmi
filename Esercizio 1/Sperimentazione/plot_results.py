import csv
from matplotlib import pyplot as plt


def save_csv(file_name, rows):
    with open(f'results/{file_name}.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(["struttura", "dimensione", "tempo"])
        writer.writerows(rows)

def read_csv(file_name):
    with open(f"results/{file_name}") as f:
        data = {"OS_LIST": {"dimensione": [], "tempo": []},
            "OS_BST":   {"dimensione": [], "tempo": []},
            "OS_AVL":   {"dimensione": [], "tempo": []}}

        with open(f"results/{file_name}") as f:
            reader = csv.DictReader(f)
            for riga in reader:
                s = riga["struttura"]
                data[s]["dimensione"].append(int(riga["dimensione"]))
                data[s]["tempo"].append(float(riga["tempo"]))
        return data

def plot(file_name):
    plot_colors = {"OS_LIST": 'crimson',
                   "OS_BST": 'teal',
                   "OS_AVL": 'goldenrod',}

    data = read_csv(file_name + ".csv")
    for struct in ["OS_LIST", "OS_BST", "OS_AVL"]:
        plt.plot(data[struct]["dimensione"],
                 data[struct]["tempo"],
                 label=struct,
                 color=plot_colors[struct])
        plt.legend()
        plt.xlabel("Dimensione (int)")
        plt.ylabel("Tempo (s)")
        plt.grid(True)
        plt.savefig("results/figures/"+file_name+"_"+struct+".pdf", bbox_inches="tight")
        plt.show()
