-- list all domain names and leads (first & last) from each site
-- SELECT sites.domain_name, leads.first_name, leads.last_name 
-- FROM sites
-- JOIN leads ON sites.id = leads.sites_id;

-- get names of clients, their domain names, and the first name of all the leads generated from those sites
-- SELECT clients.first_name AS client_name , clients.last_name, sites.domain_name, leads.first_name AS leads_name
-- FROM clients
-- JOIN sites ON clients.id = sites.clients_id
-- JOIN leads ON sites.id = leads.sites_id;

-- list all the clients and the sites that each client has, even if the client hasn't landed a site yet. 
-- SELECT clients.first_name, clients.last_name, sites.domain_name
-- FROM clients
-- LEFT JOIN sites on clients.id = sites.clients_id;

-- "GROUP BY"  and "SUM" -- "SUM()" can be replaced with "MIN()", "MAX()", "AVG()" functions as needed. 
-- SELECT clients.first_name, clients.last_name, SUM(billing.amount) AS Total_Billed
-- FROM clients
-- JOIN billing ON clients.id = billing.clients_id
-- GROUP BY clients_id;

--       GROUP CONCAT
--  list all the domians associated with each client
-- SELECT clients.first_name, clients.last_name, GROUP_CONCAT(' ', sites.domain_name) AS Domains
-- FROM clients
-- JOIN sites ON clients.id = sites.clients_id
-- GROUP BY clients.id;

--    COUNT    --
-- find total number of leads from each site
SELECT COUNT(leads.id), sites.domain_name
FROM sites
JOIN leads ON sites.id = leads.sites_id
GROUP BY sites.id;
