"""
Creator: Aleksandra Krylova
"""

package main

import (
	"bufio"
	"fmt"
	"os"
	"regexp"
	"sort"
	"strconv"
	"strings"
)

// Dictionary is type
type Dictionary struct {
	Key   string
	Value int
}

// Ny is type
type Ny []Dictionary

func (a Ny) Len() int           { return len(a) }
func (a Ny) Swap(i, j int)      { a[i], a[j] = a[j], a[i] }
func (a Ny) Less(i, j int) bool { return a[i].Value > a[j].Value }

func main() {
	var STRING string
	var SUM []string
	isAlpha := regexp.MustCompile(`^[a-z]+$`).MatchString
	scan := bufio.NewScanner(os.Stdin)
	scan.Scan()
	STRING = scan.Text()
	STRING = strings.ToLower(STRING)
	for _, s := range strings.Split(STRING, "") {
		if isAlpha(s) {
			SUM = append(SUM, s)
		}
	}
	sort.Strings(SUM)
	SYMBOLS := []Dictionary{}
	FIRST := Dictionary{
		Key:   SUM[0],
		Value: 1,
	}
	SYMBOLS = append(SYMBOLS, FIRST)
	var check bool
	for i := 1; i < len(SUM); i++ {
		check = true
		for j := 0; j < len(SYMBOLS); j++ {
			if SYMBOLS[j].Key == SUM[i] {
				SYMBOLS[j].Value++
				check = false
				break
			}
		}
		if check {
			FIRST := Dictionary{
				Key:   SUM[i],
				Value: 1,
			}
			SYMBOLS = append(SYMBOLS, FIRST)
		}
	}
	sort.Sort(Ny(SYMBOLS))
	for i := 0; i < len(SYMBOLS); i++ {
		fmt.Println(SYMBOLS[i].Key + ": " + strconv.Itoa(SYMBOLS[i].Value))
	}
}
