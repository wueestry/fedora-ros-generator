# Meta Package
Name:           ros-iron-composition
Version:        0.27.1
Release:        1%{?dist}
License:        Apache License 2.0
URL:            http://www.ros.org/
Summary:        Meta package for ros2-iron-composition and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-iron-composition
Requires:       ros2-iron-composition-devel

Obsoletes: ros-iron-composition < 0.27.1-1

%description
Examples for composing multiple nodes in a single process.

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Fri Apr 26 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - iron.0.27.1-1
- Update to latest release
