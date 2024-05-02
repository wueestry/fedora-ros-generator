# Meta Package
Name:           ros-iron-ompl
Version:        1.5.2
Release:        1%{?dist}
License:        BSD
URL:            https://ompl.kavrakilab.org
Summary:        Meta package for ros2-iron-ompl and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-iron-ompl
Requires:       ros2-iron-ompl-devel

Obsoletes: ros-iron-ompl < 1.5.2-1

%description
OMPL is a free sampling-based motion planning library.

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Fri Apr 26 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - iron.1.5.2-1
- Update to latest release
