{
  "user": {
    "fields": {
      "metadata": {
        "role": {
          "displayIf": {
            "logic": true
          }
        },
        "occupation": {
          "displayIf": {
            "logic": true
          }
        },
        "boardRegistration": {
          "displayIf": {
            "logic": true
          }
        }
      },
      "createAccessRequest": {
        "displayIf": {
          "logic": true
        }
      }
    }
  },
  "service": {
    "fields": {
      "kind": {
        "groups": [
          {
            "name": "I - CONSERVAÇÃO DE PAVIMENTO",
            "values": [
              "1"
            ]
          }
        ],
        "apiName": "kind",
        "dataType": "select",
        "displayName": "Categoria",
        "selectOptions": {
          "options": [
            {
              "name": "CONSERVAÇÃO DE PAVIMENTO",
              "value": "1"
            }
          ]
        }
      },
      "group": {
        "apiName": "group",
        "dataType": "select",
        "displayName": "Grupo",
        "selectOptions": {
          "options": [
            {
              "name": "Conservação",
              "value": "maintenance"
            },
            {
              "name": "Pavimentação",
              "value": "pavement"
            },
            {
              "name": "Drenagem",
              "value": "draining"
            },
            {
              "name": "Serviços Complementares",
              "value": "otherServices"
            }
          ]
        }
      }
    }
  },
  "inventory": {
    "filters": {}
  },
  "reporting": {
    "fields": {
      "lot": {
        "apiName": "lot",
        "dataType": "select",
        "displayName": "Lote",
        "selectOptions": {
          "options": [
            {
              "name": "Lote",
              "value": "0"
            }
          ]
        }
      },
      "lane": {
        "apiName": "lane",
        "dataType": "select",
        "displayName": "Faixa",
        "selectOptions": {
          "options": [
            {
              "name": "Faixa 1",
              "value": "1"
            },
            {
              "name": "Faixa 1 + Faixa 2",
              "value": "101"
            },
            {
              "name": "Faixa 1 + Acostamento",
              "value": "102"
            },
            {
              "name": "Faixa 1 + Faixa 2 + Acostamento",
              "value": "103"
            },
            {
              "name": "Faixa 2",
              "value": "2"
            },
            {
              "name": "Faixa 3",
              "value": "3"
            },
            {
              "name": "Faixa 4",
              "value": "4"
            },
            {
              "name": "Acostamento",
              "value": "5"
            },
            {
              "name": "Alça de entrada",
              "value": "6"
            },
            {
              "name": "Alça de saída",
              "value": "7"
            },
            {
              "name": "Balança",
              "value": "8"
            },
            {
              "name": "Viaduto",
              "value": "9"
            },
            {
              "name": "Taper",
              "value": "10"
            },
            {
              "name": "Retorno",
              "value": "12"
            },
            {
              "name": "Passagem Superior",
              "value": "14"
            },
            {
              "name": "Passagem Inferior",
              "value": "15"
            },
            {
              "name": "Ponte",
              "value": "16"
            },
            {
              "name": "Marginal direita",
              "value": "17"
            },
            {
              "name": "Marginal esquerda",
              "value": "18"
            },
            {
              "name": "Não se aplica",
              "value": "99"
            }
          ]
        }
      },
      "direction": {
        "apiName": "direction",
        "dataType": "select",
        "displayName": "Sentido",
        "selectOptions": {
          "options": [
            {
              "name": "Norte",
              "short": "N",
              "value": "0"
            },
            {
              "name": "Sul",
              "short": "S",
              "value": "1"
            },
            {
              "name": "Leste",
              "short": "L",
              "value": "2"
            },
            {
              "name": "Oeste",
              "short": "O",
              "value": "3"
            },
            {
              "name": "Ambos",
              "short": "A",
              "value": "4"
            },
            {
              "name": "Não se aplica",
              "short": "NA",
              "value": "5"
            }
          ]
        }
      },
      "occurrenceKind": {
        "apiName": "occurrenceKind",
        "dataType": "select",
        "displayName": "Natureza",
        "selectOptions": {
          "options": [
            {
              "name": "Condição de pavimento",
              "value": "1"
            },
            {
              "name": "Levantamento Paraná",
              "value": "3"
            },
            {
              "name": "Diário",
              "value": "5"
            },
            {
              "name": "Dispositivos de segurança",
              "value": "6"
            },
            {
              "name": "Sinalização",
              "value": "7"
            },
            {
              "name": "Marcos quilométricos",
              "value": "8"
            },
            {
              "name": "Inspeção",
              "value": "9"
            }
          ]
        }
      }
    },
    "filters": {
      "formDatapatologyType": {
        "apiName": "form_data.patology_type",
        "dataType": "selectMultiple",
        "displayName": "Tipo de patologia",
        "selectOptions": {
          "options": [
            {
              "name": "FC-1",
              "value": "1"
            },
            {
              "name": "FC-2",
              "value": "2"
            },
            {
              "name": "FC-3",
              "value": "3"
            },
            {
              "name": "Afundamento de trilha de roda - ATP",
              "value": "4"
            },
            {
              "name": "Afundamento localizado - ALP",
              "value": "5"
            },
            {
              "name": "Ondulação",
              "value": "6"
            },
            {
              "name": "Escorregamento",
              "value": "7"
            },
            {
              "name": "Exsudação",
              "value": "8"
            },
            {
              "name": "Desgaste",
              "value": "9"
            },
            {
              "name": "Panela",
              "value": "10"
            },
            {
              "name": "Remendo Bom",
              "value": "11"
            },
            {
              "name": "Remendo Ruim",
              "value": "12"
            },
            {
              "name": "Bombeamento de finos",
              "value": "13"
            }
          ]
        }
      }
    },
    "exporter": {
      "extraColumns": [
        {
          "key": "local",
          "header": "Local"
        },
        {
          "key": "adress",
          "header": "Endereço"
        },
        {
          "key": "state",
          "logic": {
            "if": [
              {
                "==": [
                  {
                    "var": "formData.state"
                  },
                  "1"
                ]
              },
              "Minas Gerais"
            ]
          },
          "header": "Estado"
        },
        {
          "key": "city",
          "logic": {
            "if": [
              {
                "==": [
                  {
                    "var": "formData.city"
                  },
                  "1"
                ]
              },
              "Baguari"
            ]
          },
          "header": "Município",
          "isDate": false
        },
        {
          "key": "situation",
          "logic": {
            "if": [
              {
                "==": [
                  {
                    "var": "formData.situation"
                  },
                  "1"
                ]
              },
              "Em exploração",
              {
                "==": [
                  {
                    "var": "formData.situation"
                  },
                  "2"
                ]
              },
              "Abandonada",
              {
                "==": [
                  {
                    "var": "formData.situation"
                  },
                  "3"
                ]
              },
              "Virgem",
              {
                "==": [
                  {
                    "var": "formData.situation"
                  },
                  "4"
                ]
              },
              "Área de empréstimo"
            ]
          },
          "header": "Situação"
        },
        {
          "key": "coordinates",
          "header": "Coordenadas"
        },
        {
          "key": "litogia",
          "logic": {
            "if": [
              {
                "==": [
                  {
                    "var": "formData.litogia"
                  },
                  "1"
                ]
              },
              "Em exploração",
              {
                "==": [
                  {
                    "var": "formData.litogia"
                  },
                  "2"
                ]
              },
              "Abandonada",
              {
                "==": [
                  {
                    "var": "formData.litogia"
                  },
                  "3"
                ]
              },
              "Virgem",
              {
                "==": [
                  {
                    "var": "formData.litogia"
                  },
                  "4"
                ]
              },
              "Área de empréstimo"
            ]
          },
          "header": "Litogia"
        },
        {
          "key": "alterRock",
          "logic": {
            "if": [
              {
                "==": [
                  {
                    "var": "formData.alterRock"
                  },
                  "1"
                ]
              },
              "Leve",
              {
                "==": [
                  {
                    "var": "formData.alterRock"
                  },
                  "2"
                ]
              },
              "Médio",
              {
                "==": [
                  {
                    "var": "formData.alterRock"
                  },
                  "3"
                ]
              },
              "Avançado"
            ]
          },
          "header": "Grau de alteração da rocha"
        },
        {
          "key": "connectFail",
          "logic": {
            "if": [
              {
                "==": [
                  {
                    "var": "formData.connectFail"
                  },
                  "1"
                ]
              },
              "Leve",
              {
                "==": [
                  {
                    "var": "formData.connectFail"
                  },
                  "2"
                ]
              },
              "Médio",
              {
                "==": [
                  {
                    "var": "formData.connectFail"
                  },
                  "3"
                ]
              },
              "Avançado"
            ]
          },
          "header": "Juntas e Falhas"
        },
        {
          "key": "recobrimento",
          "logic": {
            "if": [
              {
                "==": [
                  {
                    "var": "formData.recobrimento"
                  },
                  "1"
                ]
              },
              "Inexistente",
              {
                "==": [
                  {
                    "var": "formData.recobrimento"
                  },
                  "2"
                ]
              },
              "Até 2m",
              {
                "==": [
                  {
                    "var": "formData.recobrimento"
                  },
                  "3"
                ]
              },
              ">2m"
            ]
          },
          "header": "Recobrimento"
        },
        {
          "key": "relief",
          "logic": {
            "if": [
              {
                "==": [
                  {
                    "var": "formData.relief"
                  },
                  "1"
                ]
              },
              "Suave",
              {
                "==": [
                  {
                    "var": "formData.relief"
                  },
                  "2"
                ]
              },
              "Ondulado",
              {
                "==": [
                  {
                    "var": "formData.relief"
                  },
                  "3"
                ]
              },
              "Acentuado"
            ]
          },
          "header": "Relevo"
        },
        {
          "key": "pavAccess",
          "header": "Acesso Pavimento"
        },
        {
          "key": "condition",
          "logic": {
            "if": [
              {
                "==": [
                  {
                    "var": "formData.condition"
                  },
                  "1"
                ]
              },
              "Más Condições",
              {
                "==": [
                  {
                    "var": "formData.condition"
                  },
                  "2"
                ]
              },
              "Condições Razoáveis",
              {
                "==": [
                  {
                    "var": "formData.condition"
                  },
                  "3"
                ]
              },
              "Condições Boas"
            ]
          },
          "header": "Condições"
        },
        {
          "key": "areaAndVolume",
          "header": "Área/Volume  Estimado"
        },
        {
          "key": "owner",
          "header": "Proprietário"
        },
        {
          "key": "contact",
          "header": "Contato"
        },
        {
          "key": "phone",
          "header": "Telefone"
        },
        {
          "key": "notes",
          "header": "Observações"
        },
        {
          "key": "anmProcess",
          "header": "Processo ANM"
        },
        {
          "key": "explorePotential",
          "logic": {
            "if": [
              {
                "==": [
                  {
                    "var": "formData.explorePotential"
                  },
                  "1"
                ]
              },
              "Alto",
              {
                "==": [
                  {
                    "var": "formData.explorePotential"
                  },
                  "2"
                ]
              },
              "Médio",
              {
                "==": [
                  {
                    "var": "formData.explorePotential"
                  },
                  "3"
                ]
              },
              "Baixo",
              {
                "==": [
                  {
                    "var": "formData.explorePotential"
                  },
                  "4"
                ]
              },
              "Muito-Baixo",
              {
                "==": [
                  {
                    "var": "formData.explorePotential"
                  },
                  "5"
                ]
              },
              "Contra Indicada"
            ]
          },
          "header": "Potencial de Exploração"
        },
        {
          "key": "distance",
          "header": "Distância"
        },
        {
          "key": "vegetalCover",
          "logic": {
            "if": [
              {
                "==": [
                  {
                    "var": "formData.vegetalCover"
                  },
                  "1"
                ]
              },
              "Alto",
              {
                "==": [
                  {
                    "var": "formData.vegetalCover"
                  },
                  "2"
                ]
              },
              "Médio",
              {
                "==": [
                  {
                    "var": "formData.vegetalCover"
                  },
                  "3"
                ]
              },
              "Baixo",
              {
                "==": [
                  {
                    "var": "formData.vegetalCover"
                  },
                  "4"
                ]
              },
              "Muito-Baixo",
              {
                "==": [
                  {
                    "var": "formData.vegetalCover"
                  },
                  "5"
                ]
              },
              "Contra Indicada"
            ]
          },
          "header": "Cobertura Vegetal"
        },
        {
          "key": "landSlope",
          "header": "Inclinação do Terreno"
        },
        {
          "key": "proxApa",
          "logic": {
            "if": [
              {
                "==": [
                  {
                    "var": "formData.proxApa"
                  },
                  "1"
                ]
              },
              "Encontrada",
              {
                "==": [
                  {
                    "var": "formData.proxApa"
                  },
                  "2"
                ]
              },
              "Não Encontrada"
            ]
          },
          "header": "Proximidade APA"
        },
        {
          "key": "photosAssociated",
          "header": "Fotos Associadas"
        },
        {
          "key": "accessDescribe",
          "header": "Descrição do Acesso"
        },
        {
          "key": "vegetalLayer1",
          "logic": {
            "var": "formData.stepsBrief.0.vegetalLayer"
          },
          "header": "Etapas - Camada 1"
        },
        {
          "key": "vegetalLayer2",
          "logic": {
            "var": "formData.stepsBrief.1.vegetalLayer"
          },
          "header": "Etapas - Camada 2"
        },
        {
          "key": "vegetalLayer3",
          "logic": {
            "var": "formData.stepsBrief.2.vegetalLayer"
          },
          "header": "Etapas - Camada 3"
        },
        {
          "key": "areaVegetalLayer1",
          "logic": {
            "var": "formData.stepsBrief.0.areaVegetalLayer"
          },
          "header": "Etapas - Área Camada Vegetal 1"
        },
        {
          "key": "areaVegetalLayer2",
          "logic": {
            "var": "formData.stepsBrief.1.areaVegetalLayer"
          },
          "header": "Etapas - Área Camada Vegetal 2"
        },
        {
          "key": "areaVegetalLayer3",
          "logic": {
            "var": "formData.stepsBrief.2.areaVegetalLayer"
          },
          "header": "Etapas - Área Camada Vegetal 3"
        },
        {
          "key": "heightVegetalLayer1",
          "logic": {
            "var": "formData.stepsBrief.0.heightVegetalLayer"
          },
          "header": "Etapas - Espessura Média Camada Vegetal 1"
        },
        {
          "key": "heightVegetalLayer2",
          "logic": {
            "var": "formData.stepsBrief.1.heightVegetalLayer"
          },
          "header": "Etapas - Espessura Média Camada Vegetal 2"
        },
        {
          "key": "heightVegetalLayer3",
          "logic": {
            "var": "formData.stepsBrief.2.heightVegetalLayer"
          },
          "header": "Etapas - Espessura Média Camada Vegetal 3"
        },
        {
          "key": "volumeVegetalLayer1",
          "logic": {
            "*": [
              {
                "var": "formData.stepsBrief.0.heightVegetalLayer"
              },
              {
                "var": "formData.stepsBrief.0.areaVegetalLayer"
              }
            ]
          },
          "header": "Etapas - Volume Total Camada Vegetal 1"
        },
        {
          "key": "volumeVegetalLayer2",
          "logic": {
            "*": [
              {
                "var": "formData.stepsBrief.1.heightVegetalLayer"
              },
              {
                "var": "formData.stepsBrief.1.areaVegetalLayer"
              }
            ]
          },
          "header": "Etapas - Volume Total Camada Vegetal 2"
        },
        {
          "key": "volumeVegetalLayer3",
          "logic": {
            "*": [
              {
                "var": "formData.stepsBrief.2.heightVegetalLayer"
              },
              {
                "var": "formData.stepsBrief.2.areaVegetalLayer"
              }
            ]
          },
          "header": "Etapas - Volume Total Camada Vegetal 3"
        },
        {
          "key": "decapagem1",
          "logic": {
            "var": "formData.stepsBrief.0.decapagem"
          },
          "header": "Etapas - Decapagem 1"
        },
        {
          "key": "decapagem2",
          "logic": {
            "var": "formData.stepsBrief.1.decapagem"
          },
          "header": "Etapas - Decapagem 2"
        },
        {
          "key": "decapagem3",
          "logic": {
            "var": "formData.stepsBrief.2.decapagem"
          },
          "header": "Etapas - Decapagem 3"
        },
        {
          "key": "areaDecapagem1",
          "logic": {
            "var": "formData.stepsBrief.0.areaDecapagem"
          },
          "header": "Etapas - Área Decapagem 1"
        },
        {
          "key": "areaDecapagem2",
          "logic": {
            "var": "formData.stepsBrief.1.areaDecapagem"
          },
          "header": "Etapas - Área Decapagem 2"
        },
        {
          "key": "areaDecapagem3",
          "logic": {
            "var": "formData.stepsBrief.2.areaDecapagem"
          },
          "header": "Etapas - Área Decapagem 3"
        },
        {
          "key": "heightDecapagem1",
          "logic": {
            "var": "formData.stepsBrief.0.heightDecapagem"
          },
          "header": "Etapas - Espessura Média Decapagem 1"
        },
        {
          "key": "heightDecapagem2",
          "logic": {
            "var": "formData.stepsBrief.1.heightDecapagem"
          },
          "header": "Etapas - Espessura Média Decapagem 2"
        },
        {
          "key": "heightDecapagem3",
          "logic": {
            "var": "formData.stepsBrief.2.heightDecapagem"
          },
          "header": "Etapas - Espessura Média Decapagem 3"
        },
        {
          "key": "volumeDecapagem1",
          "logic": {
            "*": [
              {
                "var": "formData.stepsBrief.0.heightDecapagem"
              },
              {
                "var": "formData.stepsBrief.0.areaDecapagem"
              }
            ]
          },
          "header": "Etapas - Volume Total Decapagem 1"
        },
        {
          "key": "volumeDecapagem2",
          "logic": {
            "*": [
              {
                "var": "formData.stepsBrief.1.heightDecapagem"
              },
              {
                "var": "formData.stepsBrief.1.areaDecapagem"
              }
            ]
          },
          "header": "Etapas - Volume Total Decapagem 2"
        },
        {
          "key": "volumeDecapagem3",
          "logic": {
            "*": [
              {
                "var": "formData.stepsBrief.2.heightDecapagem"
              },
              {
                "var": "formData.stepsBrief.2.areaDecapagem"
              }
            ]
          },
          "header": "Etapas - Volume Total Decapagem 3"
        },
        {
          "key": "horizonte1",
          "logic": {
            "var": "formData.stepsBrief.0.horizonte"
          },
          "header": "Etapas - Horizonte 1"
        },
        {
          "key": "horizonte2",
          "logic": {
            "var": "formData.stepsBrief.1.horizonte"
          },
          "header": "Etapas - Horizonte 2"
        },
        {
          "key": "horizonte3",
          "logic": {
            "var": "formData.stepsBrief.2.horizonte"
          },
          "header": "Etapas - Horizonte 3"
        },
        {
          "key": "areaHorizonte1",
          "logic": {
            "var": "formData.stepsBrief.0.areaHorizonte"
          },
          "header": "Etapas - Área Horizonte 1"
        },
        {
          "key": "areaHorizonte2",
          "logic": {
            "var": "formData.stepsBrief.1.areaHorizonte"
          },
          "header": "Etapas - Área Horizonte 2"
        },
        {
          "key": "areaHorizonte3",
          "logic": {
            "var": "formData.stepsBrief.2.areaHorizonte"
          },
          "header": "Etapas - Área Horizonte 3"
        },
        {
          "key": "heightHorizonte1",
          "logic": {
            "var": "formData.stepsBrief.0.heightHorizonte"
          },
          "header": "Etapas - Espessura Média Horizonte 1"
        },
        {
          "key": "heightHorizonte2",
          "logic": {
            "var": "formData.stepsBrief.1.heightHorizonte"
          },
          "header": "Etapas - Espessura Média Horizonte 2"
        },
        {
          "key": "heightHorizonte3",
          "logic": {
            "var": "formData.stepsBrief.2.heightHorizonte"
          },
          "header": "Etapas - Espessura Média Horizonte 3"
        },
        {
          "key": "volumeHorizonte1",
          "logic": {
            "*": [
              {
                "var": "formData.stepsBrief.0.heightHorizonte"
              },
              {
                "var": "formData.stepsBrief.0.areaHorizonte"
              }
            ]
          },
          "header": "Etapas - Volume Total Horizonte 1"
        },
        {
          "key": "volumeHorizonte2",
          "logic": {
            "*": [
              {
                "var": "formData.stepsBrief.1.heightHorizonte"
              },
              {
                "var": "formData.stepsBrief.1.areaHorizonte"
              }
            ]
          },
          "header": "Etapas - Volume Total Horizonte 2"
        },
        {
          "key": "volumeHorizonte3",
          "logic": {
            "*": [
              {
                "var": "formData.stepsBrief.2.heightHorizonte"
              },
              {
                "var": "formData.stepsBrief.2.areaHorizonte"
              }
            ]
          },
          "header": "Etapas - Volume Total Horizonte 3"
        }
      ],
      "simpleExcelColumnsOrder": [],
      "photoReportDefaultOptions": [
        "roadName",
        "km",
        "endKm",
        "lat",
        "lng",
        "direction",
        "signType",
        "signName",
        "diameter",
        "side",
        "length",
        "width",
        "plateState",
        "suportMaterial",
        "suportState",
        "foundAt"
      ]
    },
    "availableFilters": [
      "has_artesp_code",
      "csp",
      "lot",
      "demandOrigin"
    ]
  },
  "construction": {
    "fields": {
      "interventionType": {
        "selectOptions": {
          "options": []
        }
      }
    }
  },
  "reportingFile": {
    "fields": {
      "kind": {
        "apiName": "kind",
        "dataType": "select",
        "displayName": "Tipo",
        "selectOptions": {
          "options": [
            {
              "name": "Inicio",
              "value": "antes"
            },
            {
              "name": "Meio",
              "value": "durante"
            },
            {
              "name": "Fim",
              "value": "depois"
            }
          ]
        }
      }
    }
  },
  "occurrenceType": {
    "fields": {
      "occurrenceKind": {
        "apiName": "occurrenceKind",
        "dataType": "select",
        "displayName": "Natureza",
        "selectOptions": {
          "options": [
            {
              "name": "Condição de pavimento",
              "value": "1"
            },
            {
              "name": "Levantamento Paraná",
              "value": "3"
            },
            {
              "name": "Diário",
              "value": "5"
            },
            {
              "name": "Dispositivos de segurança",
              "value": "6"
            },
            {
              "name": "Sinalização",
              "value": "7"
            },
            {
              "name": "Marcos quilométricos",
              "value": "8"
            },
            {
              "name": "Inspeção",
              "value": "9"
            }
          ]
        }
      }
    }
  },
  "reportingDeadline": {
    "fields": {
      "lot": {
        "apiName": "lot",
        "dataType": "select",
        "displayName": "Lote",
        "selectOptions": {
          "options": [
            {
              "name": "Lote",
              "value": "0"
            }
          ]
        }
      },
      "lane": {
        "apiName": "lane",
        "dataType": "select",
        "displayName": "Faixa",
        "selectOptions": {
          "options": [
            {
              "name": "Faixa 1",
              "value": "1"
            },
            {
              "name": "Faixa 1 + Faixa 2",
              "value": "101"
            },
            {
              "name": "Faixa 1 + Acostamento",
              "value": "102"
            },
            {
              "name": "Faixa 1 + Faixa 2 + Acostamento",
              "value": "103"
            },
            {
              "name": "Faixa 2",
              "value": "2"
            },
            {
              "name": "Faixa 3",
              "value": "3"
            },
            {
              "name": "Faixa 4",
              "value": "4"
            },
            {
              "name": "Acostamento",
              "value": "5"
            },
            {
              "name": "Alça de entrada",
              "value": "6"
            },
            {
              "name": "Alça de saída",
              "value": "7"
            },
            {
              "name": "Balança",
              "value": "8"
            },
            {
              "name": "Viaduto",
              "value": "9"
            },
            {
              "name": "Taper",
              "value": "10"
            },
            {
              "name": "Retorno",
              "value": "12"
            },
            {
              "name": "Passagem Superior",
              "value": "14"
            },
            {
              "name": "Passagem Inferior",
              "value": "15"
            },
            {
              "name": "Ponte",
              "value": "16"
            },
            {
              "name": "Marginal direita",
              "value": "17"
            },
            {
              "name": "Marginal esquerda",
              "value": "18"
            },
            {
              "name": "Não se aplica",
              "value": "99"
            }
          ]
        }
      },
      "direction": {
        "apiName": "direction",
        "dataType": "select",
        "displayName": "Sentido",
        "selectOptions": {
          "options": [
            {
              "name": "Norte",
              "short": "N",
              "value": "0"
            },
            {
              "name": "Sul",
              "short": "S",
              "value": "1"
            },
            {
              "name": "Leste",
              "short": "L",
              "value": "2"
            },
            {
              "name": "Oeste",
              "short": "O",
              "value": "3"
            },
            {
              "name": "Ambos",
              "short": "A",
              "value": "4"
            },
            {
              "name": "Não se aplica",
              "short": "NA",
              "value": "5"
            }
          ]
        }
      },
      "occurrenceKind": {
        "apiName": "occurrenceKind",
        "dataType": "select",
        "displayName": "Natureza",
        "selectOptions": {
          "options": [
            {
              "name": "Condição de pavimento",
              "value": "1"
            },
            {
              "name": "Levantamento Paraná",
              "value": "3"
            },
            {
              "name": "Diário",
              "value": "5"
            },
            {
              "name": "Dispositivos de segurança",
              "value": "6"
            },
            {
              "name": "Sinalização",
              "value": "7"
            },
            {
              "name": "Marcos quilométricos",
              "value": "8"
            },
            {
              "name": "Inspeção",
              "value": "9"
            }
          ]
        }
      }
    }
  },
  "reportingSpreadsheet": {
    "extraColumns": [
      {
        "key": "id",
        "header": "Número de emissão"
      },
      {
        "key": "uf",
        "header": "UF"
      },
      {
        "key": "cityMt",
        "header": "Município"
      },
      {
        "key": "length",
        "header": "Comprimento"
      },
      {
        "key": "height",
        "header": "Altura do topo"
      },
      {
        "key": "sideDistance",
        "header": "Distância do dispositivo ao bordo da pista"
      },
      {
        "key": "slopeDistance",
        "header": "Distância do dispositivo ao talude"
      },
      {
        "key": "obstacle",
        "header": "Tipo de obstáculo"
      },
      {
        "key": "distanceOfObstacle",
        "header": "Distância do dispositivo ao obstáculo"
      },
      {
        "key": "hasObstacleHighlighter",
        "header": "Presença de marcador de obstáculo"
      },
      {
        "key": "hasReflectiveElement",
        "header": "Presença de elemento refletivo"
      },
      {
        "key": "entranceTerminal",
        "logic": {
          "cat": [
            {
              "if": [
                {
                  "==": [
                    "1",
                    {
                      "var": "formData.entranceTerminal"
                    }
                  ]
                },
                "Terminal abatido (inclinado)",
                ""
              ]
            },
            {
              "if": [
                {
                  "==": [
                    "2",
                    {
                      "var": "formData.entranceTerminal"
                    }
                  ]
                },
                " Terminal absorvedor de energia",
                ""
              ]
            },
            {
              "if": [
                {
                  "==": [
                    "3",
                    {
                      "var": "formData.entranceTerminal"
                    }
                  ]
                },
                " Terminal atenuador de impacto",
                ""
              ]
            },
            {
              "if": [
                {
                  "==": [
                    "4",
                    {
                      "var": "formData.entranceTerminal"
                    }
                  ]
                },
                " Terminal ancorado no talude",
                ""
              ]
            },
            {
              "if": [
                {
                  "==": [
                    "5",
                    {
                      "var": "formData.entranceTerminal"
                    }
                  ]
                },
                " Terminal aéreo (válido somente para defensas)",
                ""
              ]
            },
            {
              "if": [
                {
                  "==": [
                    "6",
                    {
                      "var": "formData.entranceTerminal"
                    }
                  ]
                },
                " Sem terminal de entrada (válido somente para barreiras)",
                ""
              ]
            }
          ]
        },
        "header": "Terminal de entrada:"
      },
      {
        "key": "entranceTerminalState",
        "logic": {
          "cat": [
            {
              "if": [
                {
                  "==": [
                    "1",
                    {
                      "var": "formData.entranceTerminalState"
                    }
                  ]
                },
                "Bom ",
                ""
              ]
            },
            {
              "if": [
                {
                  "==": [
                    "2",
                    {
                      "var": "formData.entranceTerminalState"
                    }
                  ]
                },
                "Regular",
                ""
              ]
            },
            {
              "if": [
                {
                  "==": [
                    "3",
                    {
                      "var": "formData.entranceTerminalState"
                    }
                  ]
                },
                "Ruim",
                ""
              ]
            }
          ]
        },
        "header": "Estado de conservação:"
      },
      {
        "key": "entranceTerminalLength",
        "header": "Comprimento da transição de entrada"
      },
      {
        "key": "exitTerminal",
        "logic": {
          "cat": [
            {
              "if": [
                {
                  "==": [
                    "1",
                    {
                      "var": "formData.exitTerminal"
                    }
                  ]
                },
                "Terminal abatido (inclinado)",
                ""
              ]
            },
            {
              "if": [
                {
                  "==": [
                    "2",
                    {
                      "var": "formData.exitTerminal"
                    }
                  ]
                },
                " Terminal absorvedor de energia",
                ""
              ]
            },
            {
              "if": [
                {
                  "==": [
                    "3",
                    {
                      "var": "formData.exitTerminal"
                    }
                  ]
                },
                " Terminal atenuador de impacto",
                ""
              ]
            },
            {
              "if": [
                {
                  "==": [
                    "4",
                    {
                      "var": "formData.exitTerminal"
                    }
                  ]
                },
                " Terminal ancorado no talude",
                ""
              ]
            },
            {
              "if": [
                {
                  "==": [
                    "5",
                    {
                      "var": "formData.exitTerminal"
                    }
                  ]
                },
                " Terminal aéreo",
                ""
              ]
            },
            {
              "if": [
                {
                  "==": [
                    "6",
                    {
                      "var": "formData.exitTerminal"
                    }
                  ]
                },
                " Sem terminal de entrada",
                ""
              ]
            }
          ]
        },
        "header": "Terminal de saída:"
      },
      {
        "key": "exitTerminalState",
        "logic": {
          "cat": [
            {
              "if": [
                {
                  "==": [
                    "1",
                    {
                      "var": "formData.exitTerminalState"
                    }
                  ]
                },
                "Bom ",
                ""
              ]
            },
            {
              "if": [
                {
                  "==": [
                    "2",
                    {
                      "var": "formData.exitTerminalState"
                    }
                  ]
                },
                "Regular",
                ""
              ]
            },
            {
              "if": [
                {
                  "==": [
                    "3",
                    {
                      "var": "formData.exitTerminalState"
                    }
                  ]
                },
                "Ruim",
                ""
              ]
            }
          ]
        },
        "header": "Estado de conservação:"
      },
      {
        "key": "exitTerminalLength",
        "header": "Comprimento da transição de saída"
      },
      {
        "key": "pathologiesDefenses",
        "logic": {
          "cat": [
            {
              "if": [
                {
                  "in": [
                    "1",
                    {
                      "var": "formData.pathologiesDefenses"
                    }
                  ]
                },
                "Corrosão;",
                ""
              ]
            },
            {
              "if": [
                {
                  "in": [
                    "2",
                    {
                      "var": "formData.pathologiesDefenses"
                    }
                  ]
                },
                "Alinhamento;",
                ""
              ]
            },
            {
              "if": [
                {
                  "in": [
                    "3",
                    {
                      "var": "formData.pathologiesDefenses"
                    }
                  ]
                },
                "Fixação dos postes;",
                ""
              ]
            },
            {
              "if": [
                {
                  "in": [
                    "4",
                    {
                      "var": "formData.pathologiesDefenses"
                    }
                  ]
                },
                "Fixação dos parafusos;",
                ""
              ]
            }
          ]
        },
        "header": "Manifestações patológicas"
      },
      {
        "key": "lengthpathologiesDefenses1",
        "header": "Extensão de corrosão"
      },
      {
        "key": "lengthpathologiesDefenses2",
        "header": "Extensão de alinhamento"
      },
      {
        "key": "lengthpathologiesDefenses3",
        "header": "Extensão de fixação dos postes"
      },
      {
        "key": "lengthpathologiesDefenses4",
        "header": "Extensão de fixação de parafusos"
      },
      {
        "key": "actions",
        "logic": {
          "cat": [
            {
              "if": [
                {
                  "in": [
                    "1",
                    {
                      "var": "formData.actions"
                    }
                  ]
                },
                "Limpeza;",
                ""
              ]
            },
            {
              "if": [
                {
                  "in": [
                    "2",
                    {
                      "var": "formData.actions"
                    }
                  ]
                },
                "Necessita reparo;",
                ""
              ]
            },
            {
              "if": [
                {
                  "in": [
                    "3",
                    {
                      "var": "formData.actions"
                    }
                  ]
                },
                "Demais danos;",
                ""
              ]
            }
          ]
        },
        "header": "Ações a serem tomadas"
      },
      {
        "key": "patologyType",
        "logic": {
          "cat": [
            {
              "if": [
                {
                  "in": [
                    "1",
                    {
                      "var": "formData.patologyType"
                    }
                  ]
                },
                "FC-1;",
                ""
              ]
            },
            {
              "if": [
                {
                  "in": [
                    "2",
                    {
                      "var": "formData.patologyType"
                    }
                  ]
                },
                "FC-2;",
                ""
              ]
            },
            {
              "if": [
                {
                  "in": [
                    "3",
                    {
                      "var": "formData.patologyType"
                    }
                  ]
                },
                "FC-3;",
                ""
              ]
            },
            {
              "if": [
                {
                  "in": [
                    "4",
                    {
                      "var": "formData.patologyType"
                    }
                  ]
                },
                "Afundamento de trilha de roda - ATP;",
                ""
              ]
            },
            {
              "if": [
                {
                  "in": [
                    "5",
                    {
                      "var": "formData.patologyType"
                    }
                  ]
                },
                "Afundamento localizado - ALP;",
                ""
              ]
            },
            {
              "if": [
                {
                  "in": [
                    "6",
                    {
                      "var": "formData.patologyType"
                    }
                  ]
                },
                "Ondulação;",
                ""
              ]
            },
            {
              "if": [
                {
                  "in": [
                    "7",
                    {
                      "var": "formData.patologyType"
                    }
                  ]
                },
                "Escorregamento;",
                ""
              ]
            },
            {
              "if": [
                {
                  "in": [
                    "8",
                    {
                      "var": "formData.patologyType"
                    }
                  ]
                },
                "Exsudação;",
                ""
              ]
            },
            {
              "if": [
                {
                  "in": [
                    "9",
                    {
                      "var": "formData.patologyType"
                    }
                  ]
                },
                "Desgaste;",
                ""
              ]
            },
            {
              "if": [
                {
                  "in": [
                    "10",
                    {
                      "var": "formData.patologyType"
                    }
                  ]
                },
                "Panela;",
                ""
              ]
            },
            {
              "if": [
                {
                  "in": [
                    "11",
                    {
                      "var": "formData.patologyType"
                    }
                  ]
                },
                "Remendo Bom;",
                ""
              ]
            },
            {
              "if": [
                {
                  "in": [
                    "12",
                    {
                      "var": "formData.patologyType"
                    }
                  ]
                },
                "Remendo Ruim;",
                ""
              ]
            },
            {
              "if": [
                {
                  "in": [
                    "13",
                    {
                      "var": "formData.patologyType"
                    }
                  ]
                },
                "Bombeamento de finos;",
                ""
              ]
            }
          ]
        },
        "header": "Tipo de patologia"
      },
      {
        "key": "patologySide",
        "logic": {
          "cat": [
            {
              "if": [
                {
                  "==": [
                    "1",
                    {
                      "var": "formData.patologySide"
                    }
                  ]
                },
                "Trilha externa",
                ""
              ]
            },
            {
              "if": [
                {
                  "==": [
                    "2",
                    {
                      "var": "formData.patologySide"
                    }
                  ]
                },
                "Meia faixa externa",
                ""
              ]
            },
            {
              "if": [
                {
                  "==": [
                    "3",
                    {
                      "var": "formData.patologySide"
                    }
                  ]
                },
                "Eixo ",
                ""
              ]
            },
            {
              "if": [
                {
                  "==": [
                    "4",
                    {
                      "var": "formData.patologySide"
                    }
                  ]
                },
                "Trilha interna",
                ""
              ]
            },
            {
              "if": [
                {
                  "==": [
                    "5",
                    {
                      "var": "formData.patologySide"
                    }
                  ]
                },
                "Meia faixa interna",
                ""
              ]
            },
            {
              "if": [
                {
                  "==": [
                    "6",
                    {
                      "var": "formData.patologySide"
                    }
                  ]
                },
                "Faixa inteira",
                ""
              ]
            }
          ]
        },
        "header": "Localização da patologia"
      }
    ]
  },
  "serviceOrderActionStatus": {
    "fields": {
      "kind": {
        "apiName": "kind",
        "dataType": "select",
        "displayName": "Tipo",
        "selectOptions": {
          "options": [
            {
              "name": "Apontamento",
              "value": "REPORTING_STATUS"
            }
          ]
        }
      }
    }
  }
}