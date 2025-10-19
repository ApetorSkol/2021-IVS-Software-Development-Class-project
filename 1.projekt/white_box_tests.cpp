//======== Copyright (c) 2021, FIT VUT Brno, All rights reserved. ============//
//
// Purpose:     White Box - Tests suite
//
// $NoKeywords: $ivs_project_1 $white_box_code.cpp
// $Author:     JMENO PRIJMENI <xlogin00@stud.fit.vutbr.cz>
// $Date:       $2021-01-04
//============================================================================//
/**
 * @file white_box_tests.cpp
 * @author JMENO PRIJMENI
 * 
 * @brief Implementace testu prace s maticemi.
 */

#include "gtest/gtest.h"
#include "white_box_code.h"

//============================================================================//
// ** ZDE DOPLNTE TESTY **
//
// Zde doplnte testy operaci nad maticemi. Cilem testovani je:
// 1. Dosahnout maximalniho pokryti kodu (white_box_code.cpp) testy.
// 2. Overit spravne chovani operaci nad maticemi v zavislosti na rozmerech 
//    matic.
//============================================================================//

TEST( FirstTest, MatrixConstructor) 
{
	Matrix mat;
	EXPECT_EQ(mat.get(0 , 0), 0);
	Matrix mat2(2,4);
	EXPECT_EQ(mat2.get(1 , 3), 0);
	Matrix mat3(10 , 10);
	EXPECT_EQ(mat3.get(0 , 0), 0);
	EXPECT_ANY_THROW(Matrix mat4(0,0));
	EXPECT_ANY_THROW(Matrix mat5(-6,2));
        EXPECT_ANY_THROW(Matrix mat5(6,-2));

	EXPECT_ANY_THROW(mat2.get(2,4));
	EXPECT_ANY_THROW(mat2.get(-2,4));
	EXPECT_ANY_THROW(mat2.get(2,-4));
}

TEST( SecondTest, MatrixInsert)
{
        Matrix mat;
	EXPECT_TRUE(mat.set(0,0,78));
	EXPECT_EQ(mat.get(0 , 0), 78);
        EXPECT_TRUE(mat.set(0,0,-164));
 	EXPECT_EQ(mat.get(0 , 0), -164);
        EXPECT_TRUE(mat.set(0,0,-654/23));
 	EXPECT_EQ(mat.get(0 , 0), -654/23);
	EXPECT_FALSE(mat.set(-1,2,5));       
	EXPECT_FALSE(mat.set(1,-2,5));

        Matrix mat2(2,4);
        EXPECT_TRUE(mat2.set(1,2,578));
        EXPECT_EQ(mat2.get(1 , 2), 578);
        EXPECT_TRUE(mat2.set(1,1,-164));
        EXPECT_EQ(mat2.get(1 , 1), -164);
        EXPECT_TRUE(mat2.set(1,3,-6541/213));
        EXPECT_EQ(mat2.get(1 , 3), -6541/213);
        EXPECT_FALSE(mat2.set(-78,52,8765));
        EXPECT_FALSE(mat2.set(4651,-8542,555));

	Matrix mat3(122,122);
        EXPECT_TRUE(mat3.set(121,74,34678));
        EXPECT_EQ(mat3.get(121 , 74), 34678);
        EXPECT_TRUE(mat3.set(69,69,-1264));
        EXPECT_EQ(mat3.get(69 , 69), -1264);
        EXPECT_TRUE(mat3.set(46,90,-654.2134));
        EXPECT_EQ(mat3.get(46 , 90), -654.2134);
        EXPECT_FALSE(mat3.set(-17,2,5));
        EXPECT_FALSE(mat3.set(122,99,5));
	
}

TEST( ThirdTest, MatrixInserting)
{
	Matrix mat;
	std::vector<std::vector< double > > values
	{
		{1}
	};
	EXPECT_TRUE(mat.set(values));
	Matrix mat2(3,5);
	std::vector<std::vector< double > > values2
        {
                {1 ,2  ,3      ,4/3 ,5},
		{4 ,-5 ,6.1235 ,7   ,8},
		{7 ,8  ,-9     ,10  ,-11}
        };
	EXPECT_FALSE(mat2.set(values));
	EXPECT_TRUE(mat2.set(values2));
}


TEST( FourthTest, MatrixOperatorEq)
{
        Matrix mat;
        Matrix mat2;
        EXPECT_TRUE(mat.operator==(mat2));
        EXPECT_TRUE(mat2.set(0,0,-1));
        EXPECT_FALSE(mat.operator==(mat2));
        Matrix mat3(3,5);
        Matrix mat4(3,5);
        std::vector<std::vector< double > > values
        {
                {1 ,2  ,3      ,4/3 ,5},
                {4 ,-5 ,6.1235 ,7   ,8},
                {7 ,8  ,-9     ,10  ,-11}
        };
        EXPECT_TRUE(mat3.set(values));
        EXPECT_TRUE(mat4.set(values));
        EXPECT_ANY_THROW(mat.operator==(mat3));
        EXPECT_ANY_THROW(mat3.operator==(mat));
        EXPECT_TRUE(mat3.operator==(mat4));
}

TEST( FifthTest, MatrixOperatorPlus)
{
        Matrix mat;
	Matrix mat2(3,5);
        Matrix mat3(3,5);
        Matrix mat4(3,5);
	Matrix mat5(3,5);
        std::vector<std::vector< double > > values
        {
                {1 ,2  ,3   ,4  ,-5},
                {4 ,-5 ,6.1 ,7  ,8},
                {7 ,8  ,-9  ,10 ,-11.5}
        };
	std::vector<std::vector< double > > values2
        {
                {1 ,2   ,3   ,4  ,5},
                {4 ,5.5 ,6.1 ,7  ,8},
                {7 ,8   ,10  ,10 ,11.5}
        };
        EXPECT_TRUE(mat3.set(values));
        EXPECT_TRUE(mat4.set(values2));

        EXPECT_ANY_THROW(mat.operator+(mat3));
        EXPECT_ANY_THROW(mat3.operator+(mat));
        mat2=mat3.operator+(mat4);
	std::vector<std::vector< double > > values3
        {
                {2  ,4   ,6    ,8  ,0},
                {8  ,0.5 ,12.2 ,14 ,16},
                {14 ,16  ,1    ,20 ,0}
        };
	EXPECT_TRUE(mat5.set(values3));
	EXPECT_TRUE(mat2.operator==(mat5));
}

TEST( SixthTest, MatrixOperatorMulMat)
{
	Matrix mat(4,3);
	Matrix mat2(3,3);
	Matrix mat3(4,3);
	EXPECT_ANY_THROW(mat2.operator*(mat));
	EXPECT_EQ(mat3, mat3.operator*(mat2));
	EXPECT_EQ(mat, mat.operator*(mat2));
        std::vector<std::vector< double > > values
	{
		{12      ,0    ,-4},
		{54      ,12.5 ,0},
		{-138.23 ,14   ,-76},
		{12      ,0    ,78}
	};
	std::vector<std::vector< double > > values2
        {
                {2  ,0    ,-4},

                {5  ,0.43 ,449},
                {94 ,634  ,-76123}
        };
	EXPECT_TRUE(mat.set(values));
	EXPECT_TRUE(mat2.set(values2));
	std::vector<std::vector< double > > values3
        {
                {-352     ,-2536     ,304444},
                {170.5    ,5.375     ,5396.5},
                {-7350.46 ,-48177.98 ,5792186.92},
                {7356     ,49452     ,-5937642}
        };
	EXPECT_TRUE(mat3.set(values3));
	EXPECT_EQ(mat.operator*(mat2),mat3);
}

TEST(SeventhTest, MatrixOperatorMultScal)
{
	Matrix mat;
	Matrix mat2(4,3);
	Matrix mat3(4,3);
        std::vector<std::vector< double > > values
        {
                {12      ,0    ,-4},
                {54      ,12.5 ,0},
                {-138.23 ,14   ,-76},
                {12      ,0    ,78}
        };
	EXPECT_EQ(mat, mat.operator*(1151245));
        EXPECT_EQ(mat, mat.operator*(0));
        EXPECT_EQ(mat, mat.operator*(-0.12345));

        EXPECT_EQ(mat3,mat2.operator*(0));
	EXPECT_TRUE(mat2.set(values));
        std::vector<std::vector< double > > values2
        {
                {144      ,0   ,-48},
                {648      ,150 ,0},
                {-1658.76 ,168 ,-912},
                {144      ,0   ,936}
        };
	EXPECT_TRUE(mat3.set(values2));
	for (int i = 0; i<4;i++)
	{
		for(int j = 0; j<3;j++)
		{
			EXPECT_FLOAT_EQ((mat2.operator*(12)).get(i,j), mat3.get(i,j));
		}
	}
	EXPECT_EQ(mat2.operator*(0),mat3.operator*(0));
        std::vector<std::vector< double > > values3
        {
                {-12    ,0    ,4},
                {-54    ,-12.5 ,0},
                {138.23 ,-14   ,76},
                {-12     ,0    ,-78}
        };
	EXPECT_TRUE(mat3.set(values3));
	EXPECT_EQ(mat3,mat2.operator*(-1));
}

TEST(EighthTest, MatrixSolveEq)
{
	Matrix mat(3,3);
	Matrix mat2(1,3);
	Matrix mat3(4,3);
	std::vector<double> values{0,0,0};
        std::vector<double> solution{0,0,0};
	EXPECT_ANY_THROW(mat.solveEquation(values));
        std::vector<std::vector< double > > values1
        {
                {1 ,0 ,0},
                {0 ,1 ,0},
                {0 ,0 ,1}
        };
        std::vector<std::vector< double > > values2
        {
                {1 ,2 ,3}
        };
	EXPECT_TRUE(mat2.set(values2));
	EXPECT_ANY_THROW(mat2.solveEquation(values));

	EXPECT_TRUE(mat.set(values1));
	EXPECT_EQ(solution,mat.solveEquation(values));

        std::vector<double> values0{0,0,0,0};
        std::vector<std::vector< double > > values3
        {
                {1 ,0 ,0},
                {0 ,1 ,0},
                {0 ,0 ,1},
		{1 ,1 ,1}
        };
	EXPECT_TRUE(mat3.set(values3));
	EXPECT_ANY_THROW(mat3.solveEquation(values0));

}
TEST(NinethTest, MatrixTrans)
{
	Matrix mat(3,3);
	Matrix mat2(1,4);
	Matrix mat3(4,1);
	Matrix mat4(3,3);
	EXPECT_EQ((mat2.transpose()).transpose(),mat2);

        std::vector<std::vector< double > > values
        {
                {1,2,3},
                {4,5,6},
                {7,8,9}
        };
        std::vector<std::vector< double > > values2
        {
                {1,4,7},
                {2,5,8},
                {3,6,9}
        };

	EXPECT_TRUE(mat.set(values));
        EXPECT_TRUE(mat4.set(values2));
	EXPECT_EQ(mat.transpose(),mat4);
        EXPECT_EQ(mat4.transpose(),mat);
}

TEST(TenthTest, MatrixInverse)
{
	Matrix mat(3,3);
	Matrix mat2(2,2);
	Matrix mat4(2,2);
	Matrix mat2j(2,2);
	Matrix mat3j(3,3);

	Matrix mat5(6,4);
	Matrix matt;

	EXPECT_ANY_THROW(matt.inverse());
	EXPECT_ANY_THROW(mat5.inverse());

        std::vector<std::vector< double > > valuesj3
        {
                {1,0,0},
                {0,1,0},
                {0,0,1}
        };

        std::vector<std::vector< double > > valuesj2
        {
                {1,0},
                {0,1}
        };

	EXPECT_TRUE(mat2j.set(valuesj2));
        EXPECT_TRUE(mat3j.set(valuesj3));

        std::vector<std::vector< double > > values
        {
                {2,3},
                {2,2}
        };

        std::vector<std::vector< double > > values2
        {
                {-1,1.5},
                {1,-1}
        };

	EXPECT_TRUE(mat2.set(values));
        EXPECT_TRUE(mat4.set(values2));
	EXPECT_EQ(mat2.inverse(),mat4);

	Matrix matsol(2,2);

        matsol = mat2.operator*(mat2.inverse());
        for (int i = 0; i<2;i++)
        {
                for(int j = 0; j<2;j++)
                {
                        EXPECT_FLOAT_EQ(matsol.get(i,j), mat2j.get(i,j));
                }
        }

        std::vector<std::vector< double > > values3
        {
                {1,1,1},
                {0,2,3},
		{5,5,1}
        };
        EXPECT_TRUE(mat.set(values3));

	Matrix sol(3,3);

	sol = mat.operator*(mat.inverse());
        for (int i = 0; i<3;i++)
        {
                for(int j = 0; j<3;j++)
                {
                        EXPECT_FLOAT_EQ(sol.get(i,j), mat3j.get(i,j));
                }
        }


}


/*** Konec souboru white_box_tests.cpp ***/

