# Meta Package
Name:           ros-jazzy-ompl
Version:        1.5.2
Release:        1%{?dist}
License:        BSD
URL:            https://ompl.kavrakilab.org
Summary:        Meta package for ros2-jazzy-ompl and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-jazzy-ompl
Requires:       ros2-jazzy-ompl-devel

Obsoletes: ros-jazzy-ompl < 1.5.2-1

%description
OMPL is a free sampling-based motion planning library.

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Sat Apr 27 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.1.5.2-1
- Update to latest release
