$('#phone').inputmask({
    mask: '+7 (9##) ###-##-##',
    definitions: {'#': { validator: "[0-9]", cardinality: 1}},
})
