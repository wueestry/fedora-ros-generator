# Meta Package
Name:           ros-jazzy-control-toolbox
Version:        4.1.0
Release:        1%{?dist}
License:        Apache License 2.0
URL:            https://control.ros.org
Summary:        Meta package for ros2-jazzy-control_toolbox and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-jazzy-control_toolbox
Requires:       ros2-jazzy-control_toolbox-devel

Obsoletes: ros-jazzy-control-toolbox < 4.1.0-1

%description
The control toolbox contains modules that are useful across all
controllers.

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Thu Apr 10 2025 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.4.1.0-1
- Update to latest release
* Sat Mar 08 2025 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.4.0.1-1
- Update to latest release
* Mon Jan 13 2025 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.3.4.0-1
- Update to latest release
* Wed Nov 20 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.3.3.0-1
- Update to latest release
* Sat Apr 27 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.3.2.0-1
- Update to latest release
