#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Tk
%define	pnam	TableMatrix
Summary:	Tk::TableMatrix is a table/matrix widget extension to Perl/Tk
Summary(pl):	TK::TableMatrix to rozszerzenie dodające widget tabeli/macierzy do Perla/Tk
Name:		perl-Tk-TableMatrix
Version:	1.2
Release:	2
# same as perl
License:	GPL v1+ or Artistic / distributable (pTK library)
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	076a1660486806c73ad1b37ae5bbd82b
BuildRequires:	perl-Tk
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Tk::TableMatrix is a table/matrix widget extension to Perl/Tk for
displaying data in a table (or spreadsheet) format.

%description -l pl
Tk::TableMatrix to rozszerzenie dodające widget tabeli/macierzy do
Perla/Tk do wyświetlania danych w formacie tabeli lub arkusza.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	X11LIB=%{_prefix}/X11R6/%{_lib} \
	INSTALLDIRS=vendor
%{__make} \
	OPTIMIZE="%{rpmcflags}"

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog Changes README COPYING pTk/license.terms
%{perl_vendorarch}/Tk/*.pm
%dir %{perl_vendorarch}/Tk/TableMatrix
%{perl_vendorarch}/Tk/TableMatrix/Spreadsheet.pm
%{perl_vendorarch}/Tk/TableMatrix/SpreadsheetHideRows.pm
%dir %{perl_vendorarch}/auto/Tk/TableMatrix
%{perl_vendorarch}/auto/Tk/TableMatrix/*.bs
%{perl_vendorarch}/auto/Tk/TableMatrix/autosplit.ix
%attr(755,root,root) %{perl_vendorarch}/auto/Tk/TableMatrix/*.so
%{_mandir}/man3/*
# to -devel?
#%{perl_vendorarch}/Tk/pTk/mm.h
#%{perl_vendorarch}/Tk/pTk/tkTable.h
#%{perl_vendorarch}/Tk/pTk/tkTableversion.h
#%{perl_vendorarch}/Tk/pTk/version.h
#%{perl_vendorarch}/auto/Tk/pTk/extralibs.ld
