import numpy as np
import matplotlib.pyplot as plt
import pickle
import os

# Fonction pour générer les graphiques à partir de quatre dictionnaires
def generate_plots(taboue_results, recuit_results, locale_results, gloutonne_results):
    # Liste des approches
    approches = ['Tabou', 'Recuit', 'Locale', 'Gloutonne']
    
    # Extraction des critères pour chaque approche
    exec_times = [
        taboue_results['average_execution_time'],
        recuit_results['average_execution_time'],
        locale_results['average_execution_time'],
        gloutonne_results['average_execution_time']
    ]
    
    cost_solution = [
        taboue_results['average_cost'],
        recuit_results['average_cost'],
        locale_results['average_cost'],
        gloutonne_results['average_cost']
    ]
    
    
    average_proximity = [
        taboue_results['average_proximity'],
        recuit_results['average_proximity'],
        locale_results['average_proximity'],
        gloutonne_results['average_proximity']
    ]
    
    solution_diversity = [
        taboue_results['diversity'],
        recuit_results['diversity'],
        locale_results['diversity'],
        gloutonne_results['diversity']
    ]
    
    # Normalisation des valeurs pour le graphique radar
    normalized_exec_times = np.array(exec_times) / max(exec_times)
    normalized_cost_solution = np.array(cost_solution) / max(cost_solution)
    normalized_average_proximity= np.array(average_proximity) / 100
    normalized_diversity = np.array(solution_diversity) / 100

    # 1. Courbe de ligne pour le temps d'exécution
    plt.figure(figsize=(8, 6))
    plt.plot(approches, exec_times, marker='o', color='b', linestyle='-', label='Temps d\'exécution')
    plt.title('Comparaison des temps d\'exécution')
    plt.xlabel('Approches')
    plt.ylabel('Temps (s)')
    plt.grid(True)
    plt.legend()
    plt.show()



    # 2. Histogramme pour le coût de la solution obtenue
    plt.figure(figsize=(8, 6))
    plt.bar(approches, cost_solution, color='g')
    plt.title('Comparaison du coût de la solution obtenue')
    plt.xlabel('Approches')
    plt.ylabel('Coût de la solution')
    plt.grid(True)
    plt.show()
    


    # 3. Diagramme en secteurs pour la proximité moyenne
    plt.figure(figsize=(8, 6))

    plt.pie(average_proximity, labels=approches, autopct='%1.1f%%', colors=['yellow', 'orange', 'lightgreen', 'lightcoral'], startangle=90,
            wedgeprops={'edgecolor': 'black', 'linewidth':0.5 })  # Secteurs normaux avec bordure

    plt.title('Proximité moyenne des solutions', fontweight='bold', fontsize=20)
    plt.show()


    # 4. Histogramme pour la diversité des solutions
    plt.figure(figsize=(8, 6))
    plt.bar(approches, solution_diversity, color='purple')
    plt.title('Comparaison de la diversité des solutions')
    plt.xlabel('Approches')
    plt.ylabel('Diversité des solutions (%)')
    plt.grid(True)
    plt.show()

    # 5. Graphique en radar pour la comparaison des approches
    labels = ["Temps d'exécution", "Coût de la solution obtenue", "Poximité moyenne","Diversité des solutions"]
    values = [normalized_exec_times, normalized_cost_solution,normalized_average_proximity, normalized_diversity]

    # Création du graphique en radar
    angles = np.linspace(0, 2 * np.pi, len(labels), endpoint=False).tolist()
    values = np.concatenate((values, values[:1]), axis=1)
    angles += angles[:1]

    plt.figure(figsize=(6, 6))
    ax = plt.subplot(111, polar=True)
    ax.fill(angles, values[0], color='b', alpha=0.25)
    ax.plot(angles, values[0], color='b', label="Tabou")
    ax.fill(angles, values[1], color='g', alpha=0.25)
    ax.plot(angles, values[1], color='g', label="Recuit")
    ax.fill(angles, values[2], color='r', alpha=0.25)
    ax.plot(angles, values[2], color='r', label="Locale")
    ax.fill(angles, values[3], color='c', alpha=0.25)
    ax.plot(angles, values[3], color='c', label="Gloutonne")
    ax.set_yticklabels([])  # Enlever les labels des axes
    ax.set_xticks(angles[:-1])
    ax.set_xticklabels(labels)

    plt.title("Comparaison des approches")
    plt.legend()
    plt.show()


