#Overview
Thanks to +happier, the data column is now translated to english, I suggest we all use the english version
The download link for the english training set is [here](https://dl.dropboxusercontent.com/u/66809970/train_ver2_eng.csv.zip)

The table description is here:

| Eng Col Name            | Spa Col Name          | Description                                                                                                                                 |
|-------------------------|-----------------------|---------------------------------------------------------------------------------------------------------------------------------------------|
| date                    | fecha_dato            | The table is partitioned for this column                                                                                                    |
| customer_code           | ncodpers              | Customer code                                                                                                                               |
| imployee_index          | ind_empleado          | Employee index: A active, B ex employed, F filial, N not employee, P pasive                                                                 |
| country_residence       | pais_residencia       | Customer's Country residence                                                                                                                |
| sex                     | sexo                  | Customer's sex                                                                                                                              |
| age                     | age                   | Age                                                                                                                                         |
| first_holder_date       | fecha_alta            | The date in which the customer became as the first holder of a contract in the bank                                                         |
| is_new_customer         | ind_nuevo             | New customer Index. 1 if the customer registered in the last 6 months.                                                                      |
| customer_lengh_month    | antiguedad            | Customer seniority (in months)                                                                                                              |
| is_primary              | indrel                | 1 (First/Primary), 99 (Primary customer during the month but not at the end of the month)                                                   |
| last_date_as_primary    | ult_fec_cli_1t        | Last date as primary customer (if he isn't at the end of the month)                                                                         |
| customer_type           | indrel_1mes           | Customer type at the beginning of the month ,1 (First/Primary customer), 2 (co-owner ),P (Potential),3 (former primary), 4(former co-owner) |
| customer_relation_type  | tiprel_1mes           | Customer relation type at the beginning of the month, A (active), I (inactive), P (former customer),R (Potential)                           |
| is_in_same_country      | indresi               | Residence index (S (Yes) or N (No) if the residence country is the same than the bank country)                                              |
| is_foreigner            | indext                | Foreigner index (S (Yes) or N (No) if the customer's birth country is different than the bank country)                                      |
| is_spouse               | conyuemp              | Spouse index. 1 if the customer is spouse of an employee                                                                                    |
| channel                 | canal_entrada         | channel used by the customer to join                                                                                                        |
| is_deceased             | indfall               | Deceased index. N/S                                                                                                                         |
| is_primary_address      | tipodom               | Addres type. 1, primary address                                                                                                             |
| province_code           | cod_prov              | Province code (customer's address)                                                                                                          |
| province_name           | nomprov               | Province name                                                                                                                               |
| is_active               | ind_actividad_cliente | Activity index (1, active customer; 0, inactive customer)                                                                                   |
| household_income        | renta                 | Gross income of the household                                                                                                               |
| segmentation            | segmento              | segmentation: 01 - VIP, 02 - Individuals 03 - college graduated                                                                             |
| saving_account          | ind_ahor_fin_ult1     | Saving Account                                                                                                                              |
| guarantees              | ind_aval_fin_ult1     | Guarantees                                                                                                                                  |
| current_accounts        | ind_cco_fin_ult1      | Current Accounts                                                                                                                            |
| derivada_account        | ind_cder_fin_ult1     | Derivada Account                                                                                                                            |
| payroll_account         | ind_cno_fin_ult1      | Payroll Account                                                                                                                             |
| junior_account          | ind_ctju_fin_ult1     | Junior Account                                                                                                                              |
| más_particular_Account  | ind_ctma_fin_ult1     | Más particular Account                                                                                                                      |
| particular_account      | ind_ctop_fin_ult1     | particular Account                                                                                                                          |
| particular_plus_account | ind_ctpp_fin_ult1     | particular Plus Account                                                                                                                     |
| short_term_deposits     | ind_deco_fin_ult1     | Short-term deposits                                                                                                                         |
| medium_term_deposits    | ind_deme_fin_ult1     | Medium-term deposits                                                                                                                        |
| long_term_deposits      | ind_dela_fin_ult1     | Long-term deposits                                                                                                                          |
| e-account               | ind_ecue_fin_ult1     | e-account                                                                                                                                   |
| funds                   | ind_fond_fin_ult1     | Funds                                                                                                                                       |
| mortgage                | ind_hip_fin_ult1      | Mortgage                                                                                                                                    |
| pensions_1              | ind_plan_fin_ult1     | Pensions                                                                                                                                    |
| loans                   | ind_pres_fin_ult1     | Loans                                                                                                                                       |
| taxes                   | ind_reca_fin_ult1     | Taxes                                                                                                                                       |
| credit_card             | ind_tjcr_fin_ult1     | Credit Card                                                                                                                                 |
| securities              | ind_valo_fin_ult1     | Securities                                                                                                                                  |
| home_account            | ind_viv_fin_ult1      | Home Account                                                                                                                                |
| payroll                 | ind_nomina_ult1       | Payroll                                                                                                                                     |
| pensions_2              | ind_nom_pens_ult1     | Pensions                                                                                                                                    |
| direct_debit            | ind_recibo_ult1       | Direct Debit                                                                                                                                |
