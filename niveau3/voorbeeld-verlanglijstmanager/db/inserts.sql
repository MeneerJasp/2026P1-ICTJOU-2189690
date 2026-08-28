PRAGMA foreign_keys = ON;

DELETE FROM Winkel;
DELETE FROM Lijst;

-- Item
INSERT INTO Item (lijst, titel, prijs, winkel, prioriteit) VALUES
('Elektronica', 'Koptelefoon', 79.99, 'Coolblue', 1),
('Elektronica', 'Mechanisch Toetsenbord', 129.95, 'MediaMarkt', 2),
('Studie', 'Grafische Rekenmachine', 89.50, 'Amazon.nl', 1);
INSERT INTO Item (lijst, titel, prijs, winkel, prioriteit) VALUES
('Elektronica', 'Smartwatch', 199.00, 'Bol.com', 2),
('Sport', '27 inch Monitor', 349.99, 'Coolblue', 1),
('Sport', 'Rugzak', 59.95, 'MediaMarkt', 3);

-- Winkel
INSERT INTO Winkel (naam, verzendkosten) VALUES
('MediaMarkt', 3.50),
('Bol.com', 2.99),
('Coolblue', 0.00),
('Amazon.nl', 4.50);

-- Lijst
INSERT INTO Lijst (naam, budget_limiet) VALUES
('Elektronica', 500.00),
('Studie', 200.00),
('Sport', 300.00);

