from tkinter import filedialog

file_path = filedialog.askopenfilename(
    filetypes=[("Images", "*.png;*.jpg;*.jpeg;*.gif;*.bmp")]
)


    image_data = file.read()with open(file_path, "rb") as file:with open(file_path, "rb") as file:
    image_data = file.read()
    query = "INSERT INTO produits (nom, image) VALUES (%s, %s)"
params = (nom_produit, image_data)
db_connection.execute_query(query, params)


----------------------------------------------------------------------
 
% Exercice 1: PPCM de deux nombres
ppcm(A, B, PPCM) :-
    gcd(A, B, GCD),  % Utilise le prédicat prédéfini gcd/3 de SWI-Prolog
    PPCM is (A * B) // GCD.

% Exercice 2: Salaire total après N jours
salaire_total(1, 100).
salaire_total(N, Total) :-
    N > 1,
    N1 is N - 1,
    salaire_total(N1, PrevTotal),
    TodaySalary is 100 + (N - 1) * 2,
    Total is PrevTotal + TodaySalary.

% Exercice 3: Plus grand élément d'une liste
max_list([X], X).
max_list([X|Xs], Max) :-
    max_list(Xs, MaxXs),
    Max is max(X, MaxXs).

% Exercice 4: Vérifier si une liste est ordonnée (croissant ou décroissant)
is_ordered([]).
is_ordered([_]).
is_ordered([X,Y|Rest]) :-
    (X =< Y -> is_ordered([Y|Rest]) ; (X >= Y -> is_ordered([Y|Rest]) ; false).

% Exercice 5: Partie entière d'un nombre
partie_entiere(X, E) :-
    E is floor(X).

% Exercice 6: Incrémenter un nombre M fois avec un pas (version SWI-Prolog)
incrementer(0, X, _, X).
incrementer(M, X, Pas, Result) :-
    M > 0,
    NewX is X + Pas,
    M1 is M - 1,
    incrementer(M1, NewX, Pas, Result).

% Exercice 7: Calcul de l'impôt (simplifié pour SWI-Prolog)
calcul_impot(Revenu, Enfants, Marie, Impot) :-
    (Revenu =< 60000 -> Impot = 0 ;
     (Marie -> PartsConjoint = 1 ; PartsConjoint = 0),
     PartsEnfants is min(Enfants, 1) + max(0, Enfants - 1) * 0.5,
     TotalParts is 1 + PartsConjoint + PartsEnfants,
     ValeurImposable is Revenu / TotalParts,
     Impot is ValeurImposable / 3).

% Exercice 8: Calcul de la remise sur les livres
calcul_remise(NbLivres, NbInfo, Remise) :-
    (NbLivres =< 5 -> Remise = 5 ;
     NbLivres =< 10, NbInfo < 3 -> Remise = 7 ;
     NbLivres =< 10, NbInfo >= 3 -> Remise = 8 ;
     NbLivres =< 20, NbInfo < 15 -> Remise = 12 ;
     NbLivres =< 20, NbInfo >= 15 -> Remise = 15 ;
     Remise = 25).