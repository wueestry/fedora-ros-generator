# Meta Package
Name:           ros-jazzy-uncrustify-vendor
Version:        3.0.0
Release:        1%{?dist}
License:        Apache License 2.0
URL:            https://github.com/uncrustify/uncrustify
Summary:        Meta package for ros2-jazzy-uncrustify_vendor and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-jazzy-uncrustify_vendor
Requires:       ros2-jazzy-uncrustify_vendor-devel

Obsoletes: ros-jazzy-uncrustify-vendor < 3.0.0-1

%description
Wrapper around uncrustify, providing nothing but a dependency on
uncrustify, on some systems. On others, it provides an ExternalProject
build of uncrustify.

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Sat Apr 27 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.3.0.0-1
- Update to latest release
