/*
 * ----------------------------------------------------------------------
 *  Copyright (C) 2010 Numenta Inc. All rights reserved.
 *
 *  The information and source code contained herein is the
 *  exclusive property of Numenta Inc. No part of this software
 *  may be used, reproduced, stored or distributed in any form,
 *  without explicit written authorization from Numenta Inc.
 * ----------------------------------------------------------------------
 */

#ifndef NTA_FRACTION_HPP
#define NTA_FRACTION_HPP

#include <ostream>

namespace nta
{
  class Fraction
  {
  private:
    int numerator_, denominator_;
    // arbitrary cutoff -- need to fix overflow handling. 64-bits everywhere?
    const static int overflowCutoff = 10000000;
      
  public:
    Fraction(int _numerator, int _denominator);
    Fraction(int _numerator);
    Fraction();
    
    bool isNaturalNumber();
    
    int getNumerator();
    int getDenominator();
    
    void setNumerator(int _numerator);
    void setDenominator(int _denominator);
    void setFraction(int _numerator, int _denominator);
    
    static unsigned int computeGCD(int a, int b);
    static unsigned int computeLCM(int a,int b);
    
    void reduce();
    
    Fraction operator*(const Fraction& rhs);
    Fraction operator*(const int rhs);
    friend Fraction operator/(const Fraction& lhs, const Fraction& rhs);
    friend Fraction operator-(const Fraction& lhs, const Fraction& rhs);
    Fraction operator+(const Fraction& rhs);
    Fraction operator%(const Fraction& rhs);
    bool operator<(const Fraction& rhs);
    bool operator>(const Fraction& rhs);
    bool operator<=(const Fraction& rhs);
    bool operator>=(const Fraction& rhs);
    friend bool operator==(Fraction lhs, Fraction rhs);
    friend std::ostream& operator<<(std::ostream& out, Fraction rhs);
    
    static Fraction fromDouble(double value, unsigned int tolerance = 10000);
    double toDouble();
  };
}

#endif //NTA_FRACTION_HPP
