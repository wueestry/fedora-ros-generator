# Meta Package
Name:           ros-humble-control-toolbox
Version:        3.2.0
Release:        1%{?dist}
License:        BSD-3-Clause
URL:            http://ros.org/wiki/control_toolbox
Summary:        Meta package for ros2-humble-control_toolbox and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-humble-control_toolbox
Requires:       ros2-humble-control_toolbox-devel

Obsoletes: ros-humble-control-toolbox < 3.2.0-1

%description
The control toolbox contains modules that are useful across all
controllers.

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Mon Feb 19 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.3.2.0-1
- Update to latest release
* Wed Aug 23 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.3.1.0-1
- update to latest upstream release
* Wed Aug 23 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.3.1.0-1
- update to latest upstream release
* Sat Jul 01 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.3.1.0-1
- update to latest upstream release
* Sat Apr 15 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.3.0.0-1
- update to latest release
