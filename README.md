# About
This code is a quick implementation of a little parser to modify srt files in order to sync text with your video. This code has been tested to work with **Python 3**

# Usage
There's no need of instalation. Just type into your shell:
  ```bash
  python3 subtitle_time_corrector <desaired_delay> <path to the .srt file> <(optional) name appended to your file afeter conversion>
  ```
And the program will create a new .srt file with the same path in wich all the subtitles will be delayed by a time of <delay>.

# Disclaimer
There are some **final modifications** that has not be implemented yet. So, the code may not work as expected in some cases. This program is distributed in the hope that it will be useful, but **WITHOUT ANY WARRANTY**; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License 3 for more details.
