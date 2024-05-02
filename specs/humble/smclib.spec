# Meta Package
Name:           ros-humble-smclib
Version:        3.0.2
Release:        1%{?dist}
License:        Mozilla Public License Version 1.1
URL:            http://smc.sourceforge.net/
Summary:        Meta package for ros2-humble-smclib and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-humble-smclib
Requires:       ros2-humble-smclib-devel

Obsoletes: ros-humble-smclib < 3.0.2-1

%description
The State Machine Compiler (SMC) from http://smc.sourceforge.net/
converts a language-independent description of a state machine into
the source code to support that state machine. This package contains
the libraries that a compiled state machine depends on, but it does
not contain the compiler itself.

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Wed Aug 23 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.3.0.2-1
- update to latest upstream release
* Wed Aug 23 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.3.0.2-1
- update to latest upstream release
* Mon Apr 10 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.3.0.2-1
- update to latest release
* Mon Mar 20 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - noetic.1.8.6-1
- update to latest release
