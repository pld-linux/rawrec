Summary:	Record and play raw data from/to your soundcard
Summary(pl.UTF-8):	Nagrywanie i odtwarzanie surowych danych z/na karcie dźwiękowej
Name:		rawrec
Version:	0.9.98
Release:	1
License:	GPL
Group:		Applications/Sound
Source0:	http://dl.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
# Source0-md5:	15a26258853cf061e9b7e5a81f147528
URL:		http://rawrec.sourceforge.net/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
rawrec reads raw audio data from a digital signal processor (DSP) and
writes it to the given file, or to standard output if no file is
given.

rawplay reads raw audio data from the given file, or from standard
input if no file is given, and writes it to a DSP.

%description -l pl.UTF-8
rawrec wczytuje surowe dane audio z procesora sygnałowego (DSP) i
zapisuje je do podanego pliku lub na standardowe wyjście.

rawplay wczytuje surowe dane audio z pliku lub standardowego wejścia i
zapisuje je do DSP.

%prep
%setup -q

%build
%{__make} -C src \
	CC="%{__cc}" \
	OPTFLAGS="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1}

install src/rawrec $RPM_BUILD_ROOT%{_bindir}
ln -sf rawrec $RPM_BUILD_ROOT%{_bindir}/rawplay
install docs/user/rawrec.1 $RPM_BUILD_ROOT%{_mandir}/man1
echo ".so rawrec.1" > $RPM_BUILD_ROOT%{_mandir}/man1/rawplay.1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc docs/programmer/* ChangeLog
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*
