# stereo-text
Program that turns text into an stereogram image so that certain words pop out with a 3d effect.
All words in the input **marked as \<text> will be 3D.**

-----
**How to use:**

* Start it over cmd or by executing the 3dtext.py and then it allows you to type in the text
* pass the text as command line argument. (e.g. 3dtext.py "you can <enter> your text <here>" )

It works by replacing the < on the left side with different number of spaces than the version on the right.

**Examples:**
```
* Whatever space or place  * Whatever space or place  *
*  you be - Whatever life  * you  be - Whatever life  *
* you've known - What's    * you've known - What's    *
* true for you is not for  * true for you is not for  *
* me: To each,  my friend, * me: To each, my friend,  *
* their own. No matter     * their own. No matter     *
* wisdom, age, or youth, O * wisdom, age, or youth, O *
* how  you choose to test  * how you  choose to test  *
* - You'll never really    * - You'll never really    *
* find the truth. Except   * find the truth. Except   *
* that mine's  the best.   * that mine's the best.    * 
```

-----

```
Es war einmal ein <Lattenzaun>,
mit <Zwischenraum>, hindurchzuschaun.
 
Ein Architekt, der dieses sah,
stand eines Abends ploetzlich da -
 
und nahm den <Zwischenraum heraus>
und baute draus ein grosses Haus.
Der <Zaun> indessen stand ganz <dumm>
mit Latten <ohne was herum>,
 
ein Anblick graesslich und gemein.
Drum zog ihn der Senat auch ein.
 
Der <Architekt jedoch entfloh>
nach Afri - od - Ameriko.

* Es war einmal ein  Lattenzaun,    * Es war einmal ein Lattenzaun ,    *
* mit  Zwischenraum,                * mit Zwischenraum ,                *
* hindurchzuschaun.   Ein Architekt * hindurchzuschaun.   Ein Architekt *
* der dieses sah, stand eines Abend * der dieses sah, stand eines Abend *
* ploetzlich da -   und nahm den    * ploetzlich da -   und nahm den    *
*  Zwischenraum heraus und baute    * Zwischenraum heraus  und baute    *
* draus ein grosses Haus. Der  Zaun * draus ein grosses Haus. Der Zaun  *
* indessen stand ganz  dumm mit     * indessen stand ganz dumm  mit     *
* Latten  ohne was herum,   ein     * Latten ohne was herum ,   ein     *
* Anblick graesslich und gemein.    * Anblick graesslich und gemein.    *
* Drum zog ihn der Senat auch ein.  * Drum zog ihn der Senat auch ein.  *
* Der  Architekt jedoch entfloh     * Der Architekt jedoch entfloh      *
* nach Afri - od - Ameriko.         * nach Afri - od - Ameriko.         *
```

