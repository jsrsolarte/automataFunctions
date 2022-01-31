from jsonschema import validate
import jsonschema

automataSchema = {
    "$schema": "http://json-schema.org/draft-04/schema#",
    "type": "object",
    "properties": {
        "type": {
            "type": "integer"
        },
        "states": {
            "type": "array",
            "items": [
                {
                    "type": "object",
                    "properties": {
                        "name": {
                            "type": "string"
                        },
                        "acceptance": {
                            "type": "boolean"
                        }
                    },
                    "required": [
                        "name",
                        "acceptance"
                    ]
                },
                {
                    "type": "object",
                    "properties": {
                        "name": {
                            "type": "string"
                        },
                        "acceptance": {
                            "type": "boolean"
                        }
                    },
                    "required": [
                        "name",
                        "acceptance"
                    ]
                },
                {
                    "type": "object",
                    "properties": {
                        "name": {
                            "type": "string"
                        },
                        "acceptance": {
                            "type": "boolean"
                        }
                    },
                    "required": [
                        "name",
                        "acceptance"
                    ]
                },
                {
                    "type": "object",
                    "properties": {
                        "name": {
                            "type": "string"
                        },
                        "acceptance": {
                            "type": "boolean"
                        }
                    },
                    "required": [
                        "name",
                        "acceptance"
                    ]
                },
                {
                    "type": "object",
                    "properties": {
                        "name": {
                            "type": "string"
                        },
                        "acceptance": {
                            "type": "boolean"
                        }
                    },
                    "required": [
                        "name",
                        "acceptance"
                    ]
                },
                {
                    "type": "object",
                    "properties": {
                        "name": {
                            "type": "string"
                        },
                        "acceptance": {
                            "type": "boolean"
                        }
                    },
                    "required": [
                        "name",
                        "acceptance"
                    ]
                },
                {
                    "type": "object",
                    "properties": {
                        "name": {
                            "type": "string"
                        },
                        "acceptance": {
                            "type": "boolean"
                        }
                    },
                    "required": [
                        "name",
                        "acceptance"
                    ]
                },
                {
                    "type": "object",
                    "properties": {
                        "name": {
                            "type": "string"
                        },
                        "acceptance": {
                            "type": "boolean"
                        }
                    },
                    "required": [
                        "name",
                        "acceptance"
                    ]
                }
            ]
        },
        "inputs": {
            "type": "array",
            "items": [
                {
                    "type": "string"
                },
                {
                    "type": "string"
                }
            ]
        },
        "transicions": {
            "type": "array",
            "items": [
                {
                    "type": "object",
                    "properties": {
                        "state": {
                            "type": "string"
                        },
                        "inputs": {
                            "type": "array",
                            "items": [
                                {
                                    "type": "object",
                                    "properties": {
                                        "value": {
                                            "type": "string"
                                        },
                                        "to": {
                                            "type": "string"
                                        }
                                    },
                                    "required": [
                                        "value",
                                        "to"
                                    ]
                                },
                                {
                                    "type": "object",
                                    "properties": {
                                        "value": {
                                            "type": "string"
                                        },
                                        "to": {
                                            "type": "string"
                                        }
                                    },
                                    "required": [
                                        "value",
                                        "to"
                                    ]
                                }
                            ]
                        }
                    },
                    "required": [
                        "state",
                        "inputs"
                    ]
                },
                {
                    "type": "object",
                    "properties": {
                        "state": {
                            "type": "string"
                        },
                        "inputs": {
                            "type": "array",
                            "items": [
                                {
                                    "type": "object",
                                    "properties": {
                                        "value": {
                                            "type": "string"
                                        },
                                        "to": {
                                            "type": "string"
                                        }
                                    },
                                    "required": [
                                        "value",
                                        "to"
                                    ]
                                },
                                {
                                    "type": "object",
                                    "properties": {
                                        "value": {
                                            "type": "string"
                                        },
                                        "to": {
                                            "type": "string"
                                        }
                                    },
                                    "required": [
                                        "value",
                                        "to"
                                    ]
                                }
                            ]
                        }
                    },
                    "required": [
                        "state",
                        "inputs"
                    ]
                },
                {
                    "type": "object",
                    "properties": {
                        "state": {
                            "type": "string"
                        },
                        "inputs": {
                            "type": "array",
                            "items": [
                                {
                                    "type": "object",
                                    "properties": {
                                        "value": {
                                            "type": "string"
                                        },
                                        "to": {
                                            "type": "string"
                                        }
                                    },
                                    "required": [
                                        "value",
                                        "to"
                                    ]
                                },
                                {
                                    "type": "object",
                                    "properties": {
                                        "value": {
                                            "type": "string"
                                        },
                                        "to": {
                                            "type": "string"
                                        }
                                    },
                                    "required": [
                                        "value",
                                        "to"
                                    ]
                                }
                            ]
                        }
                    },
                    "required": [
                        "state",
                        "inputs"
                    ]
                },
                {
                    "type": "object",
                    "properties": {
                        "state": {
                            "type": "string"
                        },
                        "inputs": {
                            "type": "array",
                            "items": [
                                {
                                    "type": "object",
                                    "properties": {
                                        "value": {
                                            "type": "string"
                                        },
                                        "to": {
                                            "type": "string"
                                        }
                                    },
                                    "required": [
                                        "value",
                                        "to"
                                    ]
                                },
                                {
                                    "type": "object",
                                    "properties": {
                                        "value": {
                                            "type": "string"
                                        },
                                        "to": {
                                            "type": "string"
                                        }
                                    },
                                    "required": [
                                        "value",
                                        "to"
                                    ]
                                }
                            ]
                        }
                    },
                    "required": [
                        "state",
                        "inputs"
                    ]
                },
                {
                    "type": "object",
                    "properties": {
                        "state": {
                            "type": "string"
                        },
                        "inputs": {
                            "type": "array",
                            "items": [
                                {
                                    "type": "object",
                                    "properties": {
                                        "value": {
                                            "type": "string"
                                        },
                                        "to": {
                                            "type": "string"
                                        }
                                    },
                                    "required": [
                                        "value",
                                        "to"
                                    ]
                                },
                                {
                                    "type": "object",
                                    "properties": {
                                        "value": {
                                            "type": "string"
                                        },
                                        "to": {
                                            "type": "string"
                                        }
                                    },
                                    "required": [
                                        "value",
                                        "to"
                                    ]
                                }
                            ]
                        }
                    },
                    "required": [
                        "state",
                        "inputs"
                    ]
                },
                {
                    "type": "object",
                    "properties": {
                        "state": {
                            "type": "string"
                        },
                        "inputs": {
                            "type": "array",
                            "items": [
                                {
                                    "type": "object",
                                    "properties": {
                                        "value": {
                                            "type": "string"
                                        },
                                        "to": {
                                            "type": "string"
                                        }
                                    },
                                    "required": [
                                        "value",
                                        "to"
                                    ]
                                },
                                {
                                    "type": "object",
                                    "properties": {
                                        "value": {
                                            "type": "string"
                                        },
                                        "to": {
                                            "type": "string"
                                        }
                                    },
                                    "required": [
                                        "value",
                                        "to"
                                    ]
                                }
                            ]
                        }
                    },
                    "required": [
                        "state",
                        "inputs"
                    ]
                },
                {
                    "type": "object",
                    "properties": {
                        "state": {
                            "type": "string"
                        },
                        "inputs": {
                            "type": "array",
                            "items": [
                                {
                                    "type": "object",
                                    "properties": {
                                        "value": {
                                            "type": "string"
                                        },
                                        "to": {
                                            "type": "string"
                                        }
                                    },
                                    "required": [
                                        "value",
                                        "to"
                                    ]
                                },
                                {
                                    "type": "object",
                                    "properties": {
                                        "value": {
                                            "type": "string"
                                        },
                                        "to": {
                                            "type": "string"
                                        }
                                    },
                                    "required": [
                                        "value",
                                        "to"
                                    ]
                                }
                            ]
                        }
                    },
                    "required": [
                        "state",
                        "inputs"
                    ]
                },
                {
                    "type": "object",
                    "properties": {
                        "state": {
                            "type": "string"
                        },
                        "inputs": {
                            "type": "array",
                            "items": [
                                {
                                    "type": "object",
                                    "properties": {
                                        "value": {
                                            "type": "string"
                                        },
                                        "to": {
                                            "type": "string"
                                        }
                                    },
                                    "required": [
                                        "value",
                                        "to"
                                    ]
                                },
                                {
                                    "type": "object",
                                    "properties": {
                                        "value": {
                                            "type": "string"
                                        },
                                        "to": {
                                            "type": "string"
                                        }
                                    },
                                    "required": [
                                        "value",
                                        "to"
                                    ]
                                }
                            ]
                        }
                    },
                    "required": [
                        "state",
                        "inputs"
                    ]
                }
            ]
        }
    },
    "required": [
        "type",
        "states",
        "inputs",
        "transicions"
    ]
}


def validate_automata(json: str) -> dict:
    try:
        validate(json, automataSchema)
    except jsonschema.exceptions.ValidationError as err:

        return {"status": False, "message": f"Error: {err.json_path}: {err.message}"}
    return {"status": True}
