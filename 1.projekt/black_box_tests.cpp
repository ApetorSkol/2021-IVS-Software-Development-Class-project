
//======== Copyright (c) 2017, FIT VUT Brno, All rights reserved. ============//
//
// Purpose:     Red-Black Tree - public interface tests
//
// $NoKeywords: $ivs_project_1 $black_box_tests.cpp
// $Author:     JMENO PRIJMENI <xlogin00@stud.fit.vutbr.cz>
// $Date:       $2017-01-04
//============================================================================//
/**
 * @file black_box_tests.cpp
 * @author MATEJ SLIVKA
 * 
 * @brief Implementace testu binarniho stromu.
 */

#include <vector>

#include "gtest/gtest.h"

#include "red_black_tree.h"

//============================================================================//
// ** ZDE DOPLNTE TESTY **
//
// Zde doplnte testy Red-Black Tree, testujte nasledujici:
// 1. Verejne rozhrani stromu
//    - InsertNode/DeleteNode a FindNode
//    - Chovani techto metod testuje pro prazdny i neprazdny strom.
// 2. Axiomy (tedy vzdy platne vlastnosti) Red-Black Tree:
//    - Vsechny listove uzly stromu jsou *VZDY* cerne.
//    - Kazdy cerveny uzel muze mit *POUZE* cerne potomky.
//    - Vsechny cesty od kazdeho listoveho uzlu ke koreni stromu obsahuji
//      *STEJNY* pocet cernych uzlu.
//============================================================================//

class EmptyTree : public ::testing::Test
{
protected:
	 BinaryTree tree;
};

class NonEmptyTree : public ::testing::Test
{
protected:
	virtual void SetUp() {
		int values[] = { 10, 85, 15, 70, 20, 60, 30, 50, 65, 80, 90, 40, 5, 55 };
		for (int i = 0; i < 14; ++i)
			tree.InsertNode(values[i]);
	}
	BinaryTree tree;
};

class TreeAxioms : public ::testing::Test
{
protected:
	virtual void SetUp() {
		int values[] = { 10, 85, 15, 70, 20, 60, 30, 50, 65, 80, 90, 40, 5, 55 };
		for (int i = 0; i < 14; ++i)
			tree.InsertNode(values[i]);
	}
	BinaryTree tree;
};

TEST_F(EmptyTree, InsertNode)
{
	auto koren = tree.GetRoot();
	EXPECT_TRUE(koren == NULL);
	auto prirad = tree.InsertNode(1);
	EXPECT_TRUE(prirad.first);
	EXPECT_TRUE(prirad.second->key == 1);
	prirad = tree.InsertNode(1);
	EXPECT_FALSE(prirad.first);

}

TEST_F(EmptyTree, DeleteNode)
{
	EXPECT_FALSE(tree.DeleteNode(14));
}

TEST_F(EmptyTree, FindNode)
{
	EXPECT_TRUE(tree.FindNode(14) == NULL);
}

TEST_F(NonEmptyTree, InsertNode)
{
	auto prirad = tree.InsertNode(1);
	EXPECT_TRUE(prirad.first);
	EXPECT_TRUE(prirad.second->key == 1);

	prirad = tree.InsertNode(1);
	EXPECT_FALSE(prirad.first);
}
TEST_F(NonEmptyTree, DeleteNode)
{
	auto prirad = tree.DeleteNode(10); // pokusi sa odstranit existujuci prvok
	EXPECT_TRUE(prirad);
	prirad = tree.DeleteNode(1000); // pokusi sa odstranit neexistujuci prvok
	EXPECT_FALSE(prirad);
}
TEST_F(NonEmptyTree, FindNode)
{
	EXPECT_FALSE(tree.FindNode(55) == NULL); // pokusi sa najst prvok ktory existuje
	EXPECT_TRUE(tree.FindNode(14) == NULL); // pokusi sa najst prvok ktory neexistuje
}

TEST_F( TreeAxioms , Axiom1)
{
	std::vector<BinaryTree::Node_t*> outLeafNodes;
	tree.GetLeafNodes(outLeafNodes);
	for (int i = 0; i < outLeafNodes.size() - 1; i++)
	{
		EXPECT_TRUE(outLeafNodes[i]->color == BLACK);
	}
}

TEST_F(TreeAxioms, Axiom2)
{
	std::vector<BinaryTree::Node_t*> outAllNodes;
	tree.GetAllNodes(outAllNodes);
	for (int i = 0; i < outAllNodes.size() - 1; i++)
	{
		if (outAllNodes[i]->color == RED)
		{
			EXPECT_TRUE(outAllNodes[i]->pLeft->color == BLACK);
			EXPECT_TRUE(outAllNodes[i]->pRight->color == BLACK);
		}
	}
}

TEST_F(TreeAxioms, Axiom3)
{
	std::vector<BinaryTree::Node_t*> outLeafNodes;
	tree.GetLeafNodes(outLeafNodes);
	Node_t *parent;
	Node_t *root = tree.GetRoot();
	int count1 = 0, count2 = 0;

	parent = outLeafNodes[0]->pParent;
	while (parent != root)
	{
		if (parent->color == BLACK)
		{
			count1++;
		}
		parent = parent->pParent;
	}
	for (int i = 1; i < outLeafNodes.size() - 1; i++)
	{
		parent = outLeafNodes[i]->pParent;
		while (parent != root)
		{
			if (parent->color == BLACK)
			{
				count2++;
			}
			parent = parent->pParent;
		}
		EXPECT_TRUE(count1 == count2);
		count2 = 0;
	}
}

 /*** Konec souboru black_box_tests.cpp ***/

