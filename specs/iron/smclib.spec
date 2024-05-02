# Meta Package
Name:           ros-iron-smclib
Version:        4.0.0
Release:        1%{?dist}
License:        Mozilla Public License Version 1.1
URL:            http://smc.sourceforge.net/
Summary:        Meta package for ros2-iron-smclib and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-iron-smclib
Requires:       ros2-iron-smclib-devel

Obsoletes: ros-iron-smclib < 4.0.0-1

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
* Fri Apr 26 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - iron.4.0.0-1
- Update to latest release
