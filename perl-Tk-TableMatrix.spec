#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Tk
%define		pnam	TableMatrix
Summary:	Tk::TableMatrix - a table/matrix widget extension to Perl/Tk
Summary(pl.UTF-8):	TK::TableMatrix - rozszerzenie dodające widget tabeli/macierzy do Perla/Tk
Name:		perl-Tk-TableMatrix
Version:	1.23
Release:	12
# same as perl
License:	GPL v1+ or Artistic / distributable (pTK library)
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Tk/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	6b7653d129bf1a8327054a88b58d6364
URL:		http://search.cpan.org/dist/Tk-TableMatrix/
BuildRequires:	perl-Tk-devel
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Tk::TableMatrix is a table/matrix widget extension to Perl/Tk for
displaying data in a table (or spreadsheet) format.

%description -l pl.UTF-8
Tk::TableMatrix to rozszerzenie dodające widget tabeli/macierzy do
Perla/Tk do wyświetlania danych w formacie tabeli lub arkusza.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	X11LIB=%{_prefix}/X11R6/%{_lib} \
	INSTALLDIRS=vendor
%{__make} \
	CC="%{__cc}" \
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
%{perl_vendorarch}/auto/Tk/TableMatrix/autosplit.ix
%attr(755,root,root) %{perl_vendorarch}/auto/Tk/TableMatrix/*.so
%{_mandir}/man3/*
# to -devel? rm -rf as already in perl-Tk?
#%{perl_vendorarch}/Tk/pTk/mm.h
#%{perl_vendorarch}/Tk/pTk/tkTable.h
#%{perl_vendorarch}/Tk/pTk/tkTableversion.h
#%{perl_vendorarch}/Tk/pTk/version.h
#%{perl_vendorarch}/auto/Tk/pTk/extralibs.ld
