# Meta Package
Name:           ros-jazzy-control-toolbox
Version:        3.2.0
Release:        1%{?dist}
License:        BSD-3-Clause
URL:            http://ros.org/wiki/control_toolbox
Summary:        Meta package for ros2-jazzy-control_toolbox and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-jazzy-control_toolbox
Requires:       ros2-jazzy-control_toolbox-devel

Obsoletes: ros-jazzy-control-toolbox < 3.2.0-1

%description
The control toolbox contains modules that are useful across all
controllers.

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Sat Apr 27 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.3.2.0-1
- Update to latest release
