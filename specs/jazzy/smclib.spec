# Meta Package
Name:           ros-jazzy-smclib
Version:        4.1.2
Release:        1%{?dist}
License:        MPL-1.1
URL:            http://smc.sourceforge.net/
Summary:        Meta package for ros2-jazzy-smclib and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-jazzy-smclib
Requires:       ros2-jazzy-smclib-devel

Obsoletes: ros-jazzy-smclib < 4.1.2-1

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
* Sat Mar 08 2025 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.4.1.2-1
- Update to latest release
* Thu Jul 11 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.4.1.0-1
- Update to latest release
* Fri May 24 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.4.0.0-1
- Update to latest release
