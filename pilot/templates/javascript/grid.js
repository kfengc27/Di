function Grid(prefs) {
    this.element = $(prefs.element);

    var documentFragment = document.createDocumentFragment();

    var gridData = $(prefs.gridData);
    var highlightIndex = parseInt(prefs.highlightIndex) || -1;

    for (var i = 0; i < gridData.length; i++)
    {
        const element = document.createElement('div');

        // figure type
        if (i == highlightIndex)
        {
            element.className = "grid-item-highlight";
        }
        else
        {
            element.className = "grid-item";
        }
        // figure colour
        switch (gridData[i])
        {
            case 0: element.style.cssText = "background-color: white;"; break;
            case 1: element.style.cssText = "background-color: var(--red-color);"; break;
            case 2: element.style.cssText = "background-color: var(--orange-color);"; break;
            case 3: element.style.cssText = "background-color: var(--yellow-color);"; break;
            case 4: element.style.cssText = "background-color: var(--green-color);"; break;
            case 5: element.style.cssText = "background-color: var(--blue-color);"; break;
            case 6: element.style.cssText = "background-color: var(--purple-color);"; break;
            case 7: element.style.cssText = "background-color: var(--pink-color);"; break;
            default: element.style.cssText = "background-color: lightgray;"; break;
        }

        // figure inner
        if (gridData[i] > 0) {
            if (i == highlightIndex) {
                const span = document.createElement('p');
                span.style.cssText = "margin-top: -0.4rem;";
                // span.innerHTML = gridData[i].toString();
                span.innerHTML = ' ';
                element.appendChild(span);
            }
            else
                // element.innerHTML = gridData[i].toString();
                element.innerHTML = ' ';
        }
        else
            element.innerHTML = ' ';
        documentFragment.appendChild(element);
    }

    this.element.append(documentFragment);
}
