//======== Copyright (c) 2021, FIT VUT Brno, All rights reserved. ============//
//
// Purpose:     Test Driven Development - priority queue code
//
// $NoKeywords: $ivs_project_1 $tdd_code.cpp
// $Author:     JMENO PRIJMENI <xlogin00@stud.fit.vutbr.cz>
// $Date:       $2021-01-04
//============================================================================//
/**
 * @file tdd_code.cpp
 * @author JMENO PRIJMENI
 * 
 * @brief Implementace metod tridy prioritni fronty.
 */

#include <stdlib.h>
#include <stdio.h>

#include "tdd_code.h"

//============================================================================//
// ** ZDE DOPLNTE IMPLEMENTACI **
//
// Zde doplnte implementaci verejneho rozhrani prioritni fronty (Priority Queue)
// 1. Verejne rozhrani fronty specifikovane v: tdd_code.h (sekce "public:")
//    - Konstruktor (PriorityQueue()), Destruktor (~PriorityQueue())
//    - Metody Insert/Remove/Find a GetHead
//    - Pripadne vase metody definovane v tdd_code.h (sekce "protected:")
//
// Cilem je dosahnout plne funkcni implementace prioritni fronty implementovane
// pomoci tzv. "double-linked list", ktera bude splnovat dodane testy 
// (tdd_tests.cpp).
//============================================================================//

PriorityQueue::PriorityQueue()
{
	m_pHead = NULL;
}

PriorityQueue::~PriorityQueue()
{

}

void PriorityQueue::Insert(int value)
{
		auto head = GetHead();

		if (head == NULL)
		{
			m_pHead = new Element_t{ NULL,value };
			return;
		}

		if (value >= head->value)
		{
			m_pHead = new Element_t{ head,value };
			return;
		}


	while (head != NULL)
	{
		if (value >= head->pNext->value)
		{
			auto next = head->pNext;
			head->pNext = new Element_t{next,value};
			return ;
		}
		head = head->pNext;
	}
}

bool PriorityQueue::Remove(int value)
{
	auto head = GetHead();
	if (head->value == value)
	{
		m_pHead = head->pNext;
		delete head;
		return true;
	}
	while (head != NULL)
	{
		if (head->pNext->value == value)
		{
			auto temp = head->pNext;
			head->pNext = head->pNext->pNext;
			delete temp;
			return true;
		}
		head = head->pNext;
	}
    return false;
}

PriorityQueue::Element_t *PriorityQueue::Find(int value)
{
	auto head = GetHead();
	for (int i = 0; i< Length();i++)
	{
		if (head->value == value)
		{
			return head;
		}
		head = head->pNext;
	}
    return NULL;
}

size_t PriorityQueue::Length()
{
	int count = 1;
	auto head = GetHead();
	if (head == NULL)
	{
		return 0;
	}
	while ( head->pNext != NULL)
	{
		count++;
		head = head->pNext;
	}
	return count;
}

PriorityQueue::Element_t *PriorityQueue::GetHead()
{
    return m_pHead;
}

/*** Konec souboru tdd_code.cpp ***/
