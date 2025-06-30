-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Hôte : 127.0.0.1
-- Généré le : ven. 27 juin 2025 à 10:17
-- Version du serveur : 10.4.32-MariaDB
-- Version de PHP : 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de données : `salon_db`
--

-- --------------------------------------------------------

--
-- Structure de la table `approvisionnement`
--

CREATE TABLE `approvisionnement` (
  `id` int(11) NOT NULL,
  `date_approv` date NOT NULL,
  `id_produit` int(11) NOT NULL,
  `quantite` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Structure de la table `client`
--

CREATE TABLE `client` (
  `id` int(11) NOT NULL,
  `nom` varchar(30) NOT NULL,
  `prenom` varchar(30) DEFAULT NULL,
  `telephone` varchar(14) NOT NULL,
  `adresse` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Déchargement des données de la table `client`
--

INSERT INTO `client` (`id`, `nom`, `prenom`, `telephone`, `adresse`) VALUES
(1, 'MAYITOUKOU MA MAYEMBO', 'Prévu Bienheureux', '066864597', '35 rue des tes '),
(2, 'Testeur', 'Testeur', '066864598', '35 rue des test test');

-- --------------------------------------------------------

--
-- Structure de la table `employe`
--

CREATE TABLE `employe` (
  `id` int(11) NOT NULL,
  `nom` varchar(30) NOT NULL,
  `prenom` varchar(30) DEFAULT NULL,
  `salaire` int(11) DEFAULT NULL,
  `telephone` varchar(14) DEFAULT NULL,
  `id_user` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Structure de la table `prestation`
--

CREATE TABLE `prestation` (
  `id` int(11) NOT NULL,
  `date_prestation` date NOT NULL,
  `id_employe` int(11) NOT NULL,
  `id_rdv` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Structure de la table `produit`
--

CREATE TABLE `produit` (
  `id` int(11) NOT NULL,
  `libelle` varchar(50) DEFAULT NULL,
  `prix_unitaire` int(11) NOT NULL,
  `unite_mesure` int(11) DEFAULT NULL,
  `quantite` int(11) DEFAULT NULL,
  `image_prod` blob DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Déchargement des données de la table `produit`
--



-- --------------------------------------------------------

--
-- Structure de la table `produit_utilise`
--

CREATE TABLE `produit_utilise` (
  `id` int(11) NOT NULL,
  `id_produit` int(11) NOT NULL,
  `id_service_presta` int(11) NOT NULL,
  `quantite_util` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Structure de la table `rendez_vous`
--

CREATE TABLE `rendez_vous` (
  `id` int(11) NOT NULL,
  `date_prise` date NOT NULL,
  `date_rdv` date NOT NULL,
  `heure_rdv` time DEFAULT NULL,
  `objet_rdv` varchar(255) DEFAULT NULL,
  `id_client` int(11) DEFAULT NULL,
  `id_employe` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Structure de la table `service`
--

CREATE TABLE `service` (
  `id` int(11) NOT NULL,
  `img_service` varchar(255) DEFAULT NULL,
  `prix_service` int(11) NOT NULL,
  `id_type` int(11) NOT NULL,
  `description_service` varchar(255) DEFAULT NULL,
  `libelle_service` varchar(50) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Structure de la table `service_prestation`
--

CREATE TABLE `service_prestation` (
  `id` int(11) NOT NULL,
  `id_service` int(11) NOT NULL,
  `id_prestation` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Structure de la table `transaction`
--

CREATE TABLE `transaction` (
  `id` int(11) NOT NULL,
  `date_trans` date NOT NULL,
  `id_presta` int(11) DEFAULT NULL,
  `id_approv` int(11) DEFAULT NULL,
  `montant_transa` int(11) NOT NULL,
  `type_trans` varchar(20) NOT NULL,
  `libelle_trans` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Structure de la table `type_service`
--

CREATE TABLE `type_service` (
  `id` int(11) NOT NULL,
  `libelle_type` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Déchargement des données de la table `type_service`
--

INSERT INTO `type_service` (`id`, `libelle_type`) VALUES
(1, 'Esthétique');

-- --------------------------------------------------------

--
-- Structure de la table `usercompte`
--

CREATE TABLE `usercompte` (
  `id` int(11) NOT NULL,
  `user_name` varchar(30) DEFAULT NULL,
  `password` varchar(30) DEFAULT NULL,
  `secret_question` varchar(100) DEFAULT NULL,
  `sercret_answer` varchar(255) DEFAULT NULL,
  `isadmin` tinyint(1) DEFAULT 0,
  `img_profil` blob DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Index pour les tables déchargées
--

--
-- Index pour la table `approvisionnement`
--
ALTER TABLE `approvisionnement`
  ADD PRIMARY KEY (`id`),
  ADD KEY `fk_prod_approv` (`id_produit`);

--
-- Index pour la table `client`
--
ALTER TABLE `client`
  ADD PRIMARY KEY (`id`);

--
-- Index pour la table `employe`
--
ALTER TABLE `employe`
  ADD PRIMARY KEY (`id`),
  ADD KEY `fk_user_emp` (`id_user`);

--
-- Index pour la table `prestation`
--
ALTER TABLE `prestation`
  ADD PRIMARY KEY (`id`),
  ADD KEY `fk_employe` (`id_employe`),
  ADD KEY `fk_rdv` (`id_rdv`);

--
-- Index pour la table `produit`
--
ALTER TABLE `produit`
  ADD PRIMARY KEY (`id`);

--
-- Index pour la table `produit_utilise`
--
ALTER TABLE `produit_utilise`
  ADD PRIMARY KEY (`id`),
  ADD KEY `pu_prod` (`id_produit`),
  ADD KEY `pu_service` (`id_service_presta`);

--
-- Index pour la table `rendez_vous`
--
ALTER TABLE `rendez_vous`
  ADD PRIMARY KEY (`id`),
  ADD KEY `fk_client` (`id_client`),
  ADD KEY `fk_emp` (`id_employe`);

--
-- Index pour la table `service`
--
ALTER TABLE `service`
  ADD PRIMARY KEY (`id`),
  ADD KEY `fk_serice_type` (`id_type`);

--
-- Index pour la table `service_prestation`
--
ALTER TABLE `service_prestation`
  ADD PRIMARY KEY (`id`),
  ADD KEY `fk_sp_prestation` (`id_prestation`),
  ADD KEY `fk_sp_service` (`id_service`);

--
-- Index pour la table `transaction`
--
ALTER TABLE `transaction`
  ADD PRIMARY KEY (`id`),
  ADD KEY `fk_approv_trans` (`id_approv`),
  ADD KEY `fk_presta_trans` (`id_presta`);

--
-- Index pour la table `type_service`
--
ALTER TABLE `type_service`
  ADD PRIMARY KEY (`id`);

--
-- Index pour la table `usercompte`
--
ALTER TABLE `usercompte`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT pour les tables déchargées
--

--
-- AUTO_INCREMENT pour la table `approvisionnement`
--
ALTER TABLE `approvisionnement`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT pour la table `client`
--
ALTER TABLE `client`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT pour la table `employe`
--
ALTER TABLE `employe`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT pour la table `prestation`
--
ALTER TABLE `prestation`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT pour la table `produit`
--
ALTER TABLE `produit`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT pour la table `produit_utilise`
--
ALTER TABLE `produit_utilise`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT pour la table `rendez_vous`
--
ALTER TABLE `rendez_vous`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT pour la table `service`
--
ALTER TABLE `service`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT pour la table `service_prestation`
--
ALTER TABLE `service_prestation`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT pour la table `transaction`
--
ALTER TABLE `transaction`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT pour la table `type_service`
--
ALTER TABLE `type_service`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT pour la table `usercompte`
--
ALTER TABLE `usercompte`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- Contraintes pour les tables déchargées
--

--
-- Contraintes pour la table `approvisionnement`
--
ALTER TABLE `approvisionnement`
  ADD CONSTRAINT `fk_prod_approv` FOREIGN KEY (`id_produit`) REFERENCES `produit` (`id`);

--
-- Contraintes pour la table `employe`
--
ALTER TABLE `employe`
  ADD CONSTRAINT `fk_user_emp` FOREIGN KEY (`id_user`) REFERENCES `usercompte` (`id`);

--
-- Contraintes pour la table `prestation`
--
ALTER TABLE `prestation`
  ADD CONSTRAINT `fk_rdv` FOREIGN KEY (`id_rdv`) REFERENCES `rendez_vous` (`id`);

--
-- Contraintes pour la table `produit_utilise`
--
ALTER TABLE `produit_utilise`
  ADD CONSTRAINT `pu_prod` FOREIGN KEY (`id_produit`) REFERENCES `produit` (`id`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `pu_service` FOREIGN KEY (`id_service_presta`) REFERENCES `service_prestation` (`id`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Contraintes pour la table `rendez_vous`
--
ALTER TABLE `rendez_vous`
  ADD CONSTRAINT `fk_client` FOREIGN KEY (`id_client`) REFERENCES `client` (`id`),
  ADD CONSTRAINT `fk_emp` FOREIGN KEY (`id_employe`) REFERENCES `employe` (`id`);

--
-- Contraintes pour la table `service`
--
ALTER TABLE `service`
  ADD CONSTRAINT `fk_serice_type` FOREIGN KEY (`id_type`) REFERENCES `type_service` (`id`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Contraintes pour la table `service_prestation`
--
ALTER TABLE `service_prestation`
  ADD CONSTRAINT `fk_sp_prestation` FOREIGN KEY (`id_prestation`) REFERENCES `prestation` (`id`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `fk_sp_service` FOREIGN KEY (`id_service`) REFERENCES `service` (`id`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Contraintes pour la table `transaction`
--
ALTER TABLE `transaction`
  ADD CONSTRAINT `fk_approv_trans` FOREIGN KEY (`id_approv`) REFERENCES `approvisionnement` (`id`) ON DELETE SET NULL,
  ADD CONSTRAINT `fk_presta_trans` FOREIGN KEY (`id_presta`) REFERENCES `prestation` (`id`) ON DELETE SET NULL;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
