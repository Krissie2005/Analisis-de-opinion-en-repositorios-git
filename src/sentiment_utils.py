# Lexicón EN típico GitHub
positivas = {
    "fixed", "resolved", "works", "working", "works now",
    "thanks", "thank you", "great", "good", "awesome",
    "nice", "perfect", "excellent", "better", "solved",
     "fixed now", "works fine", "works perfectly",
    "great job", "awesome work", "much appreciated"
}

negativas = {
    "doesnt work", "doesn't work", "does not work", "not working",
    "broken", "crash", "crashes", "bug", "error", "issue",
    "problem", "failed", "fails", "failing", "slow",
    "freeze", "freezes", "stuck", "unable", "cannot", "can't", "worse"
}

def sentimiento_auto(texto):

    #CLASIFICA LE TEXTO COMO : (positivo, negativo y neutral)

    t = str(texto).lower() #Convierte el texto a minúsculas.
    score = 0
    for w in positivas: #Recorre el conjunto de palabras positivas (Si alguna aparece en el texto suma 1)
        if w in t:
            score += 1
    for w in negativas: #Recorre el conjunto de palabras negativas (Si alguna aparece en el texto resta 1)
        if w in t:
            score -= 1

    if score > 0:
        return "positivo"
    elif score < 0:
        return "negativo"
    else:
        return "neutral" 
    

    #El análisis de sentimiento se encapsuló en un módulo independiente basado en un 
    # enfoque léxico, permitiendo su reutilización en distintas etapas del proyecto.