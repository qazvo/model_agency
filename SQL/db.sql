CREATE TABLE IF NOT EXISTS models (
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    FIO VARCHAR(50) NOT NULL,
    gender VARCHAR(13) NOT NULL,
    phone VARCHAR(13) NOT NULL,
    height INT NOT NULL,
    weight INT NOT NULL
);
CREATE TABLE IF NOT EXISTS countries (
    id VARCHAR(3) NOT NULL PRIMARY KEY,
    name VARCHAR(20) NOT NULL
);
CREATE TABLE IF NOT EXISTS customer_organizations (
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    name VARCHAR(30) NOT NULL,
    country_id INTEGER REFERENCES countries(id),
    contact_details VARCHAR(30) NOT NULL,
    inn INT NOT NULL
);
CREATE TABLE IF NOT EXISTS events (
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    name VARCHAR(30) NOT NULL,
    country_id INTEGER REFERENCES countries(id),
  	customer_organizations_id INTEGER REFERENCES customer_organizations(id),
    date  DATE NOT NULL,
    time TIME NOT NULL
);
CREATE TABLE IF NOT EXISTS contracts(
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    event_id INTEGER REFERENCES events(id),
    model_id INTEGER REFERENCES models(id),
    payment DECIMAL(15,2)
);
CREATE TABLE IF NOT EXISTS accounts_OC(
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    login VARCHAR(20) NOT NULL,
    password VARCHAR(30) NOT NULL,
    customer_organizations_id INTEGER REFERENCES customer_organizations(id)
);
CREATE TABLE IF NOT EXISTS administrators(
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    FIO VARCHAR(50) NOT NULL,
    number_phone VARCHAR(20) NOT NULL,
    passport VARCHAR(20) NOT NULL
);
CREATE TABLE IF NOT EXISTS accounts_administrator(
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    login VARCHAR(20) NOT NULL,
    password VARCHAR(30) NOT NULL,
    administrators INTEGER REFERENCES administrators(id)
);